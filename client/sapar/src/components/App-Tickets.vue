<template>
    <div class="container-fluid py-5">
        <div class="container">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                    <th scope="col">Route</th>
                    <th scope="col">From</th>
                    <th scope="col">To</th>
                    <th scope="col">Departure Time</th>
                    <th scope="col">Arrival Time</th>
                    </tr>
                </thead>
                <tbody>

                        <tr type="button" data-bs-toggle="collapse" data-bs-target="#bus1">
                            <th scope="row">AB4958</th>
                            <td>Almaty</td>
                            <td>Taraz</td>
                            <td>10:40pm</td>
                            <td>05:30pm</td>
                            
                        </tr>   
                        <td colspan="5" class="collapse" id="bus1">
                            <div class="collapse" id="bus1">
                                    <ul class="list-group list-group-horizontal-sm">
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                    </ul>
                                    <ul class="list-group list-group-horizontal-sm">
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                    </ul>
                                    
                            </div>
                        </td>


                </tbody>
            </table>

            <table class="table table-hover text-center">
                <thead>
                    <tr>
                    <th scope="col">Route</th>
                    <th scope="col">From</th>
                    <th scope="col">To</th>
                    <th scope="col">Departure Time</th>
                    <th scope="col">Arrival Time</th>
                    <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th scope="row">AB4958</th>
                        <td>Almaty</td>
                        <td>Taraz</td>
                        <td>10:40pm</td>
                        <td>05:30pm</td>
                        <td><button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#bus2">v</button></td>
                    </tr>
                    <tr>
                        <td colspan="6" class="collapse" id="bus2">
                            <div class="collapse" id="bus2">
                                <div class="card card-body">
                                    Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
                                </div>
                            </div>
                        </td>
                    </tr>

                </tbody>
            </table>

        </div>
    </div>
    
</template>

<script>

</script>

<style scoped>  
th{
    padding-bottom: 1rem !important;
}
collapse{
    padding: none !important;
}
</style>