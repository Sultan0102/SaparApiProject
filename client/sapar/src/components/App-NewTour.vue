<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form id="createTourForm" class="mx-auto" @submit.prevent="createTour">
                        <h2 class="pt-3">{{ $t('Create a tour') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-geo-alt-fill my-auto ms-4 ms-sm-5"></i>
                            <input v-model="form.source" type="text" id="source" name="source" class="form-control" :placeholder="$t('From')">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-geo-alt-fill my-auto ms-4 ms-sm-5"></i>
                            <input v-model="form.destination" type="text" id="destination" name="destination" class="form-control" :placeholder="$t('To')">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-clock my-auto ms-4 ms-sm-5"></i>
                            <div id="weekDaysSelect" class="form-control">
                                <VueMultiSelect
                                v-model="form.weekDays"
                                :options="weekDays"
                                :multiple="true"
                                track-by="id"
                                label="name"
                                :placeholder="$t('Choose Week Days')"
                                >
                                </VueMultiSelect>
                            </div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-clock my-auto ms-4 ms-sm-5"></i>
                            <div class="form-control">
                                <VueDatePicker 
                                v-model="form.beginTime" 
                                model-auto position="left"
                                time-picker 
                                :placeholder="$t('BeginTime')" 
                                hide-input-icon
                                />
                            </div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-clock my-auto ms-4 ms-sm-5"></i>
                            <div class="form-control">
                                <VueDatePicker 
                                v-model="form.endTime" 
                                model-auto position="left" 
                                time-picker 
                                :placeholder="$t('EndTime')" 
                                hide-input-icon/>
                            </div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-pencil-fill mt-1 mb-auto ms-4 ms-sm-5"></i>
                            <input v-model="form.title" type="text" id="title" name="title" class="form-control" :placeholder="$t('Title')">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-pencil-fill mt-1 mb-auto ms-4 ms-sm-5"></i>
                            <textarea v-model="form.description" class="form-control" id="description" :placeholder="$t('Description')" rows="1"></textarea>
                        </div>

                        <div class="input-group mb-3">
                            <i class="bi bi-currency-dollar mt-1 mb-auto ms-4 ms-sm-5"></i>
                            <input v-model="form.price" type="number" id="price" name="price" class="form-control" :placeholder="$t('Price')">
                        </div>

                        <button type="submit" class="btn btn-primary mt-5 mb-3">{{ $t('Create') }}</button> <br/>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import VueMultiSelect from 'vue-multiselect'
import TourService from '@/services/TourService';
import TokenService from '@/services/TokenService';

export default {
    setup() {
        return { v$: useVuelidate() }
    },
    components: {
        VueMultiSelect
    },
    data() {
        return {
            form: {
                title: null,
                description: null,
                beginTime: null,
                endTime: null,
                source: null,
                destination: null,
                weekDays: null,
                price: null
            },
        }
    },
    computed: {
        weekDays: function() {
            let currentLanguage = this.$store.getters.getCurrentLanguage;
            let weekDays = []
            switch(currentLanguage) {
                case "en":
                    weekDays.push({id: 1, name: 'Monday'});
                    weekDays.push({id: 2, name: 'Tuesday'});
                    weekDays.push({id: 3, name: 'Wednesday'});
                    weekDays.push({id: 4, name: 'Thursday'});
                    weekDays.push({id: 5, name: 'Friday'});
                    weekDays.push({id: 6, name: 'Saturday'});
                    weekDays.push({id: 7, name: 'Sunday'});
                    break;
                case "ru":
                    weekDays.push({id: 1, name: 'Понедельник'});
                    weekDays.push({id: 2, name: 'Вторник'});
                    weekDays.push({id: 3, name: 'Среда'});
                    weekDays.push({id: 4, name: 'Четверг'});
                    weekDays.push({id: 5, name: 'Пятница'});
                    weekDays.push({id: 6, name: 'Суббота'});
                    weekDays.push({id: 7, name: 'Воскресенье'});
                    break;
                case "kz":
                    weekDays.push({id: 1, name: 'Понедельник'});
                    weekDays.push({id: 2, name: 'Вторник'});
                    weekDays.push({id: 3, name: 'Среда'});
                    weekDays.push({id: 4, name: 'Четверг'});
                    weekDays.push({id: 5, name: 'Пятница'});
                    weekDays.push({id: 6, name: 'Суббота'});
                    weekDays.push({id: 7, name: 'Воскресенье'});
                    break;
            }

            return weekDays;
        },
        currentLanguageId: function() {
            let currentLocale = this.$store.getters.getCurrentLanguage;
            let langId = null;
            switch(currentLocale) {
                case 'en':
                    langId = 3;
                    break;
                case 'kz':
                    langId = 2;
                    break;
                case 'ru':
                    langId = 1;
                    break;
                default:
                    langId = 1;
                    break;
            }
            return langId;
        },
        beginTimeStr: function() {
            let hours = String(this.form.beginTime.hours).length == 1 
                        ? '0' + this.form.beginTime.hours
                        : this.form.beginTime.hours;
            let minutes =String(this.form.beginTime.minutes).length == 1 
            ? '0' + this.form.beginTime.minutes
            : this.form.beginTime.minutes;

            
            let timeStr = `${hours}:${minutes}`

            return timeStr
        },
        endTimeStr: function() {
            let hours = String(this.form.endTime.hours).length == 1 
                        ? '0' + this.form.endTime.hours
                        : this.form.endTime.hours;
            let minutes =String(this.form.endTime.minutes).length == 1 
            ? '0' + this.form.endTime.minutes
            : this.form.endTime.minutes;

            
            let timeStr = `${hours}:${minutes}`

            return timeStr
        },
        selectedWeekDays: function() {
            let weekDaysIds = this.form.weekDays.map(w => w.id)
            return weekDaysIds
        }
    },
    methods: {
        async createTour() {
            const validationResult = await this.v$.$validate()
            if(!validationResult) {
                let errorMessages = ''
                this.v$.$errors.forEach((error)=> {
                    errorMessages+= `Field '${error.$property}'. ${error.$message} </br>`
                })

                this.$notify({
                    type: 'error',
                    title: 'Validation Error!',
                    text: errorMessages
                })
                return;
            } 
            
            const tour = {
                title: this.form.title,    
                description: this.form.description,    
                owner: TokenService.getUser().id,    
                price: this.form.price,    
                source: this.form.source,    
                destination: this.form.destination,    
                weekDays: this.selectedWeekDays,    
                beginTime: this.beginTimeStr,    
                endTime: this.endTimeStr, 
                languageId: this.currentLanguageId
            }
            
            await TourService.createTour(tour).then(
                (data)=> {
                    this.$router.push({'path': '/'})
                    this.$notify({
                        type: 'success',
                        title: 'Tour',
                        text: "Tour successfully created!"
                    })
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: 'Error',
                        text: "Tour was not created!"
                    })
                }
            )

        }
    },
    validations() {
        return {
            form: {
                title: { required },
                description: { required },
                beginTime: { required },
                endTime: { required },
                source: { required },
                destination: { required },
                weekDays: { required },
                price: { required }
            }
        }
    },

    mounted() {
        // let multiselectElement = $(".multiselect__tags");
        // multiselectElement.css('border', 'none');
    }

}

</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style scoped>
.form-select{
    background-image: none;
    
}

textarea {
	resize: vertical;
    height: 17px;
}
</style>

<style>
    #createTourForm .multiselect__tags {
        border: none;
    }
</style>