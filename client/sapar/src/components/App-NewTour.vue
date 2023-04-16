<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="createTour">
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
                            <div class="form-control">
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
                                <VueDatePicker v-model="form.time" model-auto position="left" time-picker range :placeholder="$t('Duration')" hide-input-icon/>
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

                        <button type="submit" class="btn btn-primary mt-5 mb-3">{{ $t('Create') }}</button> <br/>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import VueMultiSelect from 'vue-multiselect'

export default {
    components: {
        VueMultiSelect
    },
    data() {
        return {
            form: {
                title: null,
                description: null,
                time: null,
                source: null,
                destination: null,
                weekDays: null
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
        }
    },
    methods: {
        createTour() {
            console.log(this.form)
        }
    },

    mounted() {

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
