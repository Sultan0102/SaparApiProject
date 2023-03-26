<template>
    <div class="carousel-item" data-bs-interval="false">
        <div class="container-fluid">
            <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
                <form :id="'ticket-person-form-' + ticket.id" class="text-center mt-5 mx-auto" @submit.prevent="confirmClick">
                    <div v-if="cachedTicketPersons && cachedTicketPersons.length > 0">
                        <h2 class="pt-3">{{ $t('Order confirmation') }}</h2>
                        <div class="mt-3 py-4">
                            <select v-model="form.cachedPerson" @change="onChooseCachedPerson($event)" id="cachedPersonDropDown" class="mx-auto form-select">
                                <option selected disabled class="selected" value="0">{{ $t('Choose passengers') }}</option>

                                <option v-for="cachedPerson in cachedTicketPersons"
                                :key="cachedPerson.id"
                                :value="cachedPerson.id"
                                >
                                {{ cachedPerson.firstName + ' ' + cachedPerson.lastName }}

                                </option>
                                <option value="-1" @click="clearForm()">{{ $t('Add a new passenger') }}</option>

                            </select>
                        </div>
                    </div>
                    <h2 class="pt-3">{{ $t('Passenger Information') }} </h2>
                    <h3>for seat №{{ ticket.seatNumber }}</h3>
                    <div class="mb-3">
                        <input v-model="form.firstName" type="text" class="form-control mx-auto" name="firstName" placeholder="Vasia" :readonly="form.cachedPerson == 0 && cachedTicketPersons.length > 0">
                    </div>
                    <div class="mb-3">
                        <input v-model="form.lastName" type="text" class="form-control mx-auto" name="lastName" placeholder="Pupkin" :readonly="form.cachedPerson == 0 && cachedTicketPersons.length > 0">
                    </div>
                    <div class="mb-3">
                        <input v-model="form.secondName" type="text" class="form-control mx-auto" name="lastName" placeholder="Poluektovich" :readonly="form.cachedPerson == 0 && cachedTicketPersons.length > 0">
                    </div>
                    <select v-model="form.documentType" :id="'passportTypeDropDown_'+ticket.id" name="passportTypeDropDown" class="mx-auto form-select mb-3" :readonly="form.cachedPerson == 0 && cachedTicketPersons.length > 0">
                        <option selected disabled value="0">{{ $t('Document Type') }}</option>
                        <option  v-for="passportType in passportTypes"
                        :key="passportType.id"
                        :value="passportType.id"
                        >{{ $t(passportType.typeName) }}</option>
                    </select>   
                    <div class="mb-3">
                        <input v-model="form.documentNumber" type="text" class="form-control mx-auto" name="documentNumber" placeholder="Document Number" :readonly="form.documentType == 0 || (form.cachedPerson == 0 && cachedTicketPersons.length > 0)" >
                    </div>
                    <button v-if='!isLast' class="btn btn-primary my-3" data-bs-target="#carouselExampleDark" data-bs-slide="next">{{ $t('Next') }}</button><br/>
                    <button v-if='index!=0' class="btn btn-primary my-3" data-bs-target="#carouselExampleDark" data-bs-slide="prev">{{ $t('Previous') }}</button><br/>
                    <button v-if="isLast" class="btn btn-primary mt-3 mb-5" >{{ $t('Confirm') }}</button>
                </form>
            </div>
        </div>
    </div>
</template>


<script>

import { useVuelidate } from '@vuelidate/core'
import { required, helpers } from '@vuelidate/validators'


export default {
    props: ['index', 'ticket', 'cachedTicketPersons', 'passportTypes', 'isLast', 'confirmCallback'],
    setup() {
        return { v$: useVuelidate() }
    },
    data() {
        return {
            form: {
                firstName: '',
                lastName: '',
                secondName: '',
                documentType: 0,
                documentNumber: '',
                cachedPerson: 0,
            }
        }
    },
    computed: {
        currentDocumentFormat: function() {
            if(documentType == 0) return ''

            let documentType = this.passportTypes.filter(t => t.id == this.documentType)[0]
            return documentType.format
        }
    },
    validations() {
        return {
            form: {
                firstName: { required },
                lastName: { required },
                secondName: { required },
                documentNumber: { required },
            }
        }
    },
    methods: {
        checkProps() {
            console.log(this.ticket)
            console.log(this.index)
            console.log(this.cachedTicketPersons)
            console.log(this.passportTypes)
            console.log(this.isLast)
        },
        checkData() {
            console.log(this.form)
        },
        clearForm() {
            this.form.firstName = '';
            this.form.lastName = '';
            this.form.secondName = '';
            this.form.documentType = 0;
            this.form.documentNumber = '';
            this.form.cachedPerson = 0;
        },
        onChooseCachedPerson(event) {
            this.clearForm();
            const selectedValue = event.target.value; 
            this.form.cachedPerson = selectedValue
            
            if(selectedValue == -1) return;

            const cachedTicketPerson = this.cachedTicketPersons.filter(p => p.id == selectedValue)[0]
            console.log(cachedTicketPerson)
            this.form.firstName = cachedTicketPerson.firstName 
            this.form.lastName = cachedTicketPerson.lastName 
            this.form.secondName = cachedTicketPerson.secondName 
            this.form.documentType = cachedTicketPerson.passportNumberType 
            this.form.documentNumber = cachedTicketPerson.passportNumber
            // const cachedPerson = 
            
        },

        confirmClick() {
            this.confirmCallback();
        }


    },
    mounted(){
        console.log('Mount child')
    }
}

</script>

<style scoped>

</style>