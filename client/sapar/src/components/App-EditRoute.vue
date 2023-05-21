<template>
    <div class="container-fluid mt-lg-2 mt-1">
        <div class="container">
            <div class="container-fluid">
                <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
                    <form class="text-center mt-5 mx-auto">
                        <h2 class="py-3">ABFJHK509946</h2>
                        <div class="pb-3">
                            <select class="mx-auto form-select">
                                <option selected disabled class="selected">{{ $t('Choose source') }}</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select class="mx-auto form-select">
                                <option selected disabled class="selected">{{ $t('Choose destination') }}</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select class="mx-auto form-select">
                                <option selected disabled class="selected">{{ $t('Choose Bus') }}</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select class="mx-auto form-select">
                                <option selected disabled class="selected">{{ $t('Choose Driver') }}</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                        </div>
                        <div class="form-check mt-2 mx-auto text-start">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                {{ $t('Disabled') }}
                            </label>
                        </div>
                        <button disabled type="submit" class="btn btn-primary mt-5 mb-4">{{ $t('Apply') }}</button> <br/>
                        <button disabled type="submit" class="btn btn-primary mb-5">{{ $t('Delete') }}</button>
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

<style scoped>
.bi-caret-left-fill, .bi-caret-right-fill{
	color: #1C5E3C !important;
    font-size: 48px;
}
.disabled{
    opacity: 0.5;
}
.btn-primary{
    min-width: 250px;
}
.multiselect, .form-check{
 width: 80%;
}
</style>