<template>
    <div class="container-fluid py-5">
        <div class="container">
            <div>
            <!-- Using modifiers -->
            <b-button v-b-toggle.collapse-2 class="m-1">Toggle Collapse</b-button>

            <!-- Using value -->
            <b-button v-b-toggle="'collapse-2'" class="m-1">Toggle Collapse</b-button>

            <!-- Element to collapse -->
            <b-collapse id="collapse-2">
                <b-card>I am collapsible content!</b-card>
            </b-collapse>
            </div>
            <p>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                Button with data-bs-target
            </button>
            </p>
            <div class="collapse" id="collapseExample">
            <div class="card card-body">
                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
            </div>
        </div>
    </div>

</template>

<script>

</script>

<style scoped>

</style>