import Api from "./Api"


class ApplicationService{
    createApplication(application) {
        return Api.applications.post('', application).then(
            (response) => {
                return response.data
            }
        );
    }

    getUserApplications(criteria) {
        return Api.applications.post('user/', criteria).then(
            (response) => {
                return response.data
            }
        )
    }

    getDriverApplications() {
        return Api.applications.post('drivers/').then(
            (response) => {
                return response.data
            }
        )
    }

}

export default new ApplicationService()