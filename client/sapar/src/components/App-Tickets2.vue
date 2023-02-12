<template>
  <div class="bus-layout mt-5">
    <div class="d-flex flex-row" v-for="row in rows">
      <div
        v-for="(seat, index) in row"
        class="seat"
        :key="index"
        :class="{ selected: seat === selectedSeat }"
        @click="selectSeat(seat)"
      >
        {{ seat }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      seats: [
        "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11",
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11",
        // ...
      ],
      selectedSeat: null,
      rows: []
    };
  },
  mounted() {
    this.rows = this.seats.reduce((acc, cur, index) => {
      const rowIndex = Math.floor(index / 11);
      if (!acc[rowIndex]) acc[rowIndex] = [];
      acc[rowIndex].push(cur);
      return acc;
    }, []);
  },
  methods: {
    selectSeat(seat) {
      this.selectedSeat = seat;
    }
  }
};
</script>

<style scoped>
.selected{
  background-color: #57896F;
  color: #FFF !important;
  cursor: pointer;
}
</style>
