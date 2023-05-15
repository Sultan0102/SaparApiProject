import Api from "./Api"


class DocumentService{
    uploadDocument(formData) {
        return Api.documents.post('', 
        formData, 
        {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(
            (response) => {
                return response.data
            }
        );
    }

}

export default new DocumentService()