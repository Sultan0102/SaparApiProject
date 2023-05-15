import Api from "./Api"

class OrderService{
    createOrder(order) {
        return Api.orders.post('', {
            user: order.userId,
            schedule: order.scheduleId,
            ticket_ids: order.ticket_ids
        }).then((response) => {
            return response.data
        })
    }

    retreive(id) {
        return Api.orders.get(`${id}/`)
        .then((response)=> {
            return response.data;
        })
    }

    getUserOrders(depth=0) {
        return Api.orders.get('?depth='+depth).then(
            (response)=> {
                return response.data;
            }
        )
    }
}

export default new OrderService()