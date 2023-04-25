<template>
    <div class="container-fluid pt-5" v-if="schedule && tour">
        <div class="container mt-5">
            <h1 class="text-center">{{ schedule.route.sourceName }}<i class="bi bi-caret-right-fill"></i> {{ schedule.route.destinationName }} Tour</h1>
            <div class="row">
                <div class="col-md-6">
                    <h2 class="my-1">{{ $t('When?') }}</h2>
                    <h3 class="mb-4">{{ formattedBeginDate }} </h3>
                    <h2 class="my-1">{{ $t('Where?') }}</h2>
                    <h3 class="mb-4">Sayran Terminal</h3>
                    <h2 class="my-1">{{ $t("What's interesting?") }}</h2>
                    <ul class="mb-4">
                        {{ formattedDescription }}
                    </ul>
                </div>
                <div class="col-md-6 my-auto text-center">
                    <img src="../assets/Kolsai-Lakes.jpg" class="img-fluid w-75">
                </div>
            </div>
            <div class="text-center">
            <h2 class="my-1 mt-4">{{ $t('Still have questions?') }}</h2>
            <h3 class="mb-4">{{ $t('Contact our tour manager') }}: 87089802877</h3>
            <router-link class="nav-link" aria-current="page" to="/tour-tickets">
                <button type="button" class="btn btn-primary mb-5">{{ $t('Go back') }}</button>
            </router-link>
            
            </div>
        </div>
    </div>
</template>

<script>
import TourService from '@/services/TourService';

    export default {
        props: ['scheduleId'],
        data() {
            return {
                tour: null,
                schedule: null
            }
        },
        computed: {
            formattedBeginDate: function() {
                let currentLanguage = this.$store.getters.getCurrentLanguage;
                let beginDate = new Date(this.schedule.beginDate)
                return beginDate.toLocaleDateString(currentLanguage, {
                    month: 'long',
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit'
                })
            },
            formattedDescription: function() {
                let currentLanguage = this.$store.getters.getCurrentLanguage;
                let langId = null;
                switch(currentLanguage) {
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
                let description = this.tour.description.codeResourceValues.filter(v => v.language == langId)
                
                description = description.length == 0 
                ? this.tour.description.defaultValue
                : description[0].value
                
                return description
            }
        },
        methods: {
            async getTour() {
                
                await TourService.retreiveByScheduleId(this.scheduleId).then(
                    (data)=> {
                        this.tour = data
                        this.schedule = data.schedules[0]
                        console.log(this.schedule)
                    }
                )
            }
        },
        async mounted() {
            await this.getTour();
            console.log(this.scheduleId)
        }
    }
</script>

<style scoped>
.container{
    max-width: 800px;
    background-color: #FFFFFF;
}
h3, li{
    opacity: 0.8;
}
.img-fluid{
    box-shadow: 12px 12px #1C5E3C;
}
</style>


