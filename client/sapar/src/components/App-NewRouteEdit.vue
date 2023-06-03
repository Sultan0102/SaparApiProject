<template>
    <div v-if="schedule && destinationLocations && sourceLocations && buses && drivers" class="container-fluid mt-lg-2 mt-1">
        <div class="container">
            <div class="container-fluid">
                <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
                    <form class="text-center mt-5 mx-auto" @submit.prevent="updateSchedule">
                        <h2 class="py-3">{{ schedule.scheduleNumber }}</h2>
                        <div class="pb-3">
                            <select v-model="form.source" class="mx-auto form-select">
                                <option selected disabled value="0">{{ $t('Choose source') }}</option>
                                <option v-for="sourceLocation in sourceLocations"
                                :key="sourceLocation.id"
                                :value="sourceLocation.id"
                                >
                                {{ getLocationText(sourceLocation) }}
                                </option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select v-model="form.destination" class="mx-auto form-select" >
                                <option selected disabled value="0">{{ $t('Choose destination') }}</option>
                                <option v-for="destinationLocation in destinationLocations"
                                :key="destinationLocation.id"
                                :value="destinationLocation.id"
                                >
                                    {{ getLocationText(destinationLocation) }}
                                </option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select v-model="form.bus" class="mx-auto form-select">
                                <option selected disabled value="0">{{ $t('Choose Bus') }}</option>
                                <option v-for="bus in buses"
                                :key="bus.id"
                                :value="bus.id"
                                >
                                    {{ bus.name }}
                                </option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <select v-model="form.driver" class="mx-auto form-select">
                                <option selected disabled value="0" >{{ $t('Choose Driver') }}</option>
                                <option v-for="driver in drivers"
                                :key="driver.id"
                                :value="driver.id"
                                >
                                    {{ `${driver.user.firstName} ${driver.user.lastName}` }}
                                </option>
                            </select>
                        </div>
                        <div class="pb-3">
                            <VueMultiSelect
                                v-model="form.weekDay"
                                :options="weekDays"
                                track-by="id"
                                label="name"
                                :placeholder="$t('Choose Week Day')"
                                class="mx-auto"
                                >
                            </VueMultiSelect>
                        </div>
                        <div class="input-group mb-3">
                            <div class="form-control mx-auto">
                                <VueDatePicker v-model="form.beginTime" 
                                time-picker 
                                position="left" 
                                :placeholder="$t('Start Time')" 
                                hide-input-icon 
                                />
                            </div>
                        </div>
                        <div class="input-group mb-3">
                            <div class="form-control mx-auto">
                                <VueDatePicker v-model="form.endTime" 
                                time-picker 
                                position="left" 
                                :placeholder="$t('End Time')" 
                                hide-input-icon />
                            </div>
                        </div>
                        <div class="form-check form-control mt-2 mx-auto text-start d-flex justify-content-between">
                            <div>
                                <input v-model="form.disabled" class="form-check-input" type="checkbox" id="flexCheckDefault">
                                <label class="form-check-label" for="flexCheckDefault">
                                    {{ $t('Disabled') }}
                                </label>
                            </div>
                            
                            <i class="bi bi-info-circle" title="Creates Tickets if enabled!" @click="$notify({
                                type: 'warning',
                                title: 'Tickets',
                                text: 'Creates Tickets if enabled!'
                            })"></i>
                            
                        </div>
                        <button type="submit" class="btn btn-primary mt-5 mb-4">{{ $t('Apply') }}</button> <br/>
                        <button type="submit" class="btn btn-primary mb-5">{{ $t('Delete') }}</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
</template>


<script>
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { not } from '@vuelidate/validators';
import VueMultiSelect from 'vue-multiselect'
import TourService from '@/services/TourService';
import TokenService from '@/services/TokenService';
import RouteService from '@/services/RouteService';
import UserService from '@/services/UserService';
import { sameAs } from '@vuelidate/validators';
import ScheduleService from '@/services/ScheduleService';

export default {
    props: ['scheduleId'],
    setup() {
        return { v$: useVuelidate() }
    },
    components: {
        VueMultiSelect
    },
    data() {
        return {
            form: {
                beginTime: null,
                endTime: null,
                source: 0,
                destination: 0,
                weekDay: null,
                driver: 0,
                bus: 0,
                disabled: false
            },
            schedule: null,
            destinationLocations: [],
            sourceLocations: [],
            buses: [],
            drivers: []
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
        selectedDriver: function() {
            if (this.form.driver == 0) return null;

            let driverObj = this.drivers.filter(d => d.id == this.form.driver)[0]

            return driverObj.user.id
        },
        selectedBus: function() {
            if (this.form.bus == 0) return null;

            return this.form.bus
        }
    },
    methods: {
        async updateSchedule() {
            console.log(this.form);
            let isValid = await this.v$.$validate();
            var additionalErrorMessage = ''
            if(!this.form.disabled && (this.form.bus == 0 || this.form.driver == 0)) {
                isValid = false
                additionalErrorMessage += "Fields driver and bus are required when updating with 'disabled' unchecked</br>";
            }

            if(!isValid) {
                let errorMessages = ''
                this.v$.$errors.forEach((error)=> {
                    errorMessages += `Field '${error.$property}'. ${error.$message} </br>`
                })

                this.$notify({
                    type: 'error',
                    title: 'Validation Error!',
                    text: errorMessages+=additionalErrorMessage
                })
                return;
            }
            
            const criteria = {
                scheduleId: this.schedule.id,
                source: this.form.source,
                destination: this.form.destination,
                weekDay: this.form.weekDay.id,
                beginTime: this.beginTimeStr,
                endTime: this.endTimeStr,
                driver: this.selectedDriver,
                bus: this.selectedBus,
                disabled: this.form.disabled
            }

            await ScheduleService.updateIntercitySchedule(criteria).then(
                (data)=> {
                    this.$router.push({'name': 'RoutesAdminPanel'})
                    this.$notify({
                        type: 'success',
                        title: 'Edit Route!',
                        text: 'Successfullt Edited Route'
                    })
                }
            )
        },

        async deleteSchedule() {

        },

        getFormattedDate(dateStr) {
            let date = new Date(dateStr)

            let hours = date.getHours();
            let minutes = date.getMinutes();

            return {hours, minutes}
        },

        getLocationText(location) {
            let value = null;

            value = location.nameCode.codeResourceValues.filter(rv => rv.languageId == this.currentLanguageId)

            if(value && value.length > 0) return value[0].value;

            value = location.nameCode.codeResourceValues.filter(rv => rv.languageId == 3)

            if(value && value.length > 0) return value[0].value

            return location.nameCode.defaultValue
        },

        async getIntercityLocations() {
            await RouteService.retreiveLocations().then(
                (data)=> {

                    this.destinationLocations = data.filter(l => l.type.id == 1)
                    this.sourceLocations = data.filter(l => l.type.id == 1)
                }
            )
        },
        async getBuses() {
            await RouteService.retreiveBuses().then(
                (data)=> {
                    this.buses = data;
                }
            )
        },
        async getDrivers() {
            await UserService.retreiveDrivers().then(
                (data)=> {
                    this.drivers = data
                }
            )
        },
        async getDriver(id) {
            let driver = null

            if(!id) return driver

            await UserService.retreiveDriverByUserId(id).then(
                (data)=> {
                    driver = data
                }
            )
            return driver
        },

        async getSchedule() {
            await ScheduleService.retreive(this.scheduleId).then(
                (data)=>{
                    this.schedule = data
                },
                (error)=> {

                }
            )
            console.log(this.schedule);
            
            let driver = await this.getDriver(this.schedule.driver?.id)
            let weekDay = this.weekDays.filter(w => w.id == new Date(this.schedule.beginDate).getDay()+1)[0]  
            console.log(weekDay);
            
            this.form.bus = this.schedule.bus?.id ?? 0
            this.form.driver =  driver?.id ?? 0
            this.form.destination = this.schedule.route.destination.id
            this.form.source = this.schedule.route.source.id
            this.form.beginTime = this.getFormattedDate(this.schedule.beginDate)
            this.form.endTime = this.getFormattedDate(this.schedule.endDate)
            this.form.weekDay = weekDay
            this.form.disabled = !this.schedule.isActive
        }
    },
    validations() {
        return {
            form: {
                beginTime: { required },
                endTime: { required }   ,
                source: { required, notChosen: not(sameAs(0)),  },
                destination: { required, notChosen: not(sameAs(0)) },
                weekDay: { required }
            },
        }
    },

    async mounted() {
        await this.getSchedule()
        await this.getIntercityLocations()
        await this.getBuses()
        await this.getDrivers()
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
.multiselect{
 width: 80%;
}
</style>