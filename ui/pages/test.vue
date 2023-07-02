<template>
  <div>
    <v-card v-for="card in paginatedCards" :key="card.id">
    </v-card>
    <v-pagination v-model="currentPage"
    :total-visible="5"
    :length="Math.ceil(totalCards / cardsPerPage)"
    @input="fetchCards" >
    </v-pagination>
  </div>
</template>
<script>
export default {
  data() {
    return {
      cards: [],
      currentPage: 1,
      cardsPerPage: 10,
    };
  },
  computed: {
    totalCards() {
      return this.cards.length;
    },
    paginatedCards() {
      const startIndex = (this.currentPage - 1) * this.cardsPerPage;
      const endIndex = startIndex + this.cardsPerPage;
      return this.cards.slice(startIndex, endIndex);
    },
  },
  methods: {

  mounted() {
    this.fetchCards();
  },
}
}
 </script>
