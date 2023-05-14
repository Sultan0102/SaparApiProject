<template>
    <div class="container-fluid mb-4 pb-4">
        <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="applyApplication">
                        <h2 class="pt-3">{{ $t('Guide information') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                            <input v-model="form.email" type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="form.firstName" type="text" id="firstName" name="firstName" class="form-control" placeholder="Vasia">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="form.lastName" type="text" id="lastName" name="lastName" class="form-control" placeholder="Pupkin">
                        </div>

                        <input type="file" id="actual-file-input" hidden @change="handleFileChange($event)"/>
                        <button type="button" class="btn btn-secondary mb-3 mt-5" @click="clickOnActualFileInput"><i class="bi bi-file-earmark white me-2"></i>{{ $t('Upload CV') }} </button><br/>
                        <button class="btn btn-primary mb-3 mt-3">{{ $t('Approve') }}</button>
                        
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators';
import DocumentService from "@/services/DocumentService"
import ApplicationService from '@/services/ApplicationService';
import TourService from '@/services/TourService';
import UserService from '@/services/UserService';
import TokenService from '@/services/TokenService';

export default {
    props: ['tourId'],
    setup() {
        return { v$: useVuelidate() }
    },
    data() {
        return {
            form: {
                email: null,
                firstName: null,
                lastName: null,
                cv_file: null
            },
            tour: null
        }
    },

    validations() {
        return {
            form: {
                email: { required },
                firstName: { required },
                lastName: { required }
            }
        }
        
    },

    methods: {
        async getTour() {
            await TourService.retreiveById(this.tourId).then(
                (data)=> {
                    this.tour = data
                }
            )
        },
        async getGuide() {
            await UserService.retreiveGuideByUserId(this.guideId).then(
                (data)=> {
                    return data
                }
            )

            return null
        },  
        async applyApplication() {
            console.log(this.form)
            const isValid = await this.v$.$validate()
            if(!isValid) {
                let errorMessages = ''
                this.v$.$errors.forEach((error)=> {
                    errorMessages += `Field '${error.$property}'. ${error.$message} </br>`
                })

                this.$notify({
                    type: 'error',
                    title: 'Validation Error!',
                    text: errorMessages
                })
                return;
            }
            const userId = TokenService.getUser().id
            let formData = new FormData()
            formData.append('file', this.cv_file)
            formData.append('owner', userId)
            
            debugger;
            const applicationData = {
                guide: await this.getGuide().id,
                email: this.form.email,
                firstName: this.form.firstName,
                lastName: this.form.lastName,
                tour: this.tourId
            }

            let applicationRequest = {
                senderUser: userId,
                receiverUser: this.tour.owner,
                status: 1,
                type: 1,
                applicationData: applicationData,
                documents: []
            }

            
            await DocumentService.uploadDocument(formData).then(
                (data)=> {
                    applicationRequest.documents.push(data.id);
                    ApplicationService.createApplication(applicationRequest).then(
                        (data)=> {
                            this.$router.push({ path: '/' })
                            this.$notify({
                                type: "success", 
                                text: 'Successfully created application for hiring!'
                            })
                        },
                        (error)=> {
                            this.$notify({
                                type: "error",
                                title: "Application Creation Error!", 
                                text: 'Error while creating application!'
                            })
                        }
                    )
                },
                (error)=> {
                    this.$notify({
                        type: "error",
                        title: "Validation Error!", 
                        text: 'Error Downloading file!'
                    })
                }
            )
            
        },

        clickOnActualFileInput() {
            document.getElementById("actual-file-input").click()
        },

        handleFileChange(event) {
            this.cv_file = event.target.files[0]
        }
    },

    async mounted() {
       await this.getTour();
    }
}

</script>

<style scoped>
.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
i{
    font-size: 24px;
}
.btn-secondary{
    border-radius: 0px !important;
	background: none !important;
	border-color: #1C5E3C !important;
	border-width: 2px;
    color: #1C5E3C !important;
    min-width: 300px;
    font-size: 24px;
}
h6{
    opacity: 0.5;
}
</style>
