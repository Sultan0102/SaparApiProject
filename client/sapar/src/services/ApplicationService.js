import Api from "./Api"


class ApplicationService{
    createApplication(application) {
        return Api.applications.post('', application).then(
            (response) => {
                return response.data
            }
        );
    }

    getApplications(criteria) {
        return Api.applications.post('user/', criteria).then(
            (response) => {
                return response.data
            }
        )
    }

}

export default new ApplicationService()