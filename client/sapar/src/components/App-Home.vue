<template>
    <div class="container-fluid py-5">
        <div class="container">
            <div class="row">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{user.name}}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{{user.lastName}}</h6>

                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <button class="card-link" @click="fetchUser()" style="color:black;">Another link</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <p>{{ $t('hello') }}</p>
</template>


<script>

export default {
    data() {
        return {
            user: {
                name: "Some Name",
                lastName: "Some Last Name"
            }
        }
    },
    methods: {
        async fetchUser() {
            
            let result = null;

            await this.axios.get("https://randomuser.me/api/").then( (response) => {
                result = response;
            });

            this.user.name = result.data.results[0].name.first;
            this.user.lastName = result.data.results[0].name.last;
        }
    },
    async mounted() {
        await this.fetchUser();
        
    }
}
</script>

