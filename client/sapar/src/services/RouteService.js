import Api from "./Api"
import store from "@/store";

class RouteService{

    retreiveByOrderId(orderId) {
        let currentLanguage = store.getters.getCurrentLanguage;
        return Api.routes.post(`order/${orderId}/`, {
            languageId: currentLanguage
        }).then(
            (response)=> {
                return response.data
            }
        )
    }
    
    retreive(id) {
        return Api.routes.get(`${id}/`).then(
            (response)=> {
                return response.data
            }
        )
    }

}

export default new RouteService()