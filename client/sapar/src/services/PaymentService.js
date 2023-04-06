import Api from "./Api"


class PaymentService{
    createPayment(payment) {
        return Api.payments.post('', {
            method: payment.method,
            payDate: payment.payDate,
            payedAmount: payment.paymentAmount,
            order: payment.orderId,
            user: payment.userId
        }).then((response) => {
            return response.data
        })
    }

}

export default new PaymentService()