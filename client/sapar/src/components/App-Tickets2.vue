<template>
  <div>
    <p>Source: {{ source }}</p>
    <p>Destination: {{ destination }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      ticketData: null,
      source: null,
      destination: null,
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/post_ticket/3/1')
      .then(response => {
        this.ticketData = response.data;
        this.source = response.data.route.source.nameCode.value;
        this.destination = response.data.route.destination.nameCode.value;
      })
      .catch(error => {
        console.log(error);
      });
  }
}
</script>
