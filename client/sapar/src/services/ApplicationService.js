import Api from "./Api"


class ApplicationService{
    createApplication(application) {
        return Api.applications.post('', application).then(
            (response) => {
                return response.data
            }
        );
    }

    retreive(id) {
        return Api.applications.get(`${id}/`).then(
            (response) => {
                return response.data
            }
        );
    }

    retreiveWithDepth() {
        return Api.applications.get('', { params: {depth: 1} }).then(
            (response) => {
                return response.data
            }
        );
    }

    retreiveApplicationTypes() {
        return Api.applications.get('types/').then(
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

    updateApplicationStatus(criteria) {
        return Api.applications.patch('status/', criteria).then(
            (response)=> {
                return response.data
            }
        )
    }

}

export default new ApplicationService()