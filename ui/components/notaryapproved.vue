<template>
  <v-container>
    <v-container v-if="show">
      <v-list density="compact">
        <v-list-item
          v-for="profile in paginatedProfiles"
          :key="profile.email"
          :value="profile.email"
          active-color="primary"
        >
          <v-list-item-title v-text="profile.name"></v-list-item-title>
          <v-list-item-subtitle v-text="profile.email"></v-list-item-subtitle>
          <v-btn icon @click="view(profile.email)">
            <v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon>
          </v-btn>
        </v-list-item>
      </v-list>
      <v-container class="text-center">
        <v-pagination
          v-model="currentPage"
          :total-visible="5"
          :length="totalPages"
          @input="changePage"
        ></v-pagination>
      </v-container>
    </v-container>
    <v-container v-if="hide">
      <h2 class="text-center" style="color: darkblue;">No Profiles</h2>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "NotaryApproved",

  data() {
    return {
      currentPage: 1,
      pageSize: 5,
      profiles: [],
      requests: {},
      notary_email: null,
      notary_name: null,
      wallet: 0,
      show: false,
      hide: false,
    };
  },

  async mounted() {
    this.$vuetify.theme.dark = false;
    await this.fetchProfiles();
  },

  computed: {
    totalPages() {
      return Math.ceil(this.profiles.length / this.pageSize);
    },
    paginatedProfiles() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.profiles.slice(startIndex, endIndex);
    },
  },

  methods: {
    async fetchProfiles() {
      try {
        const response = await this.$axios.get("http://127.0.0.1:8000/verifiedusers");
        this.profiles = response.data.list;
        this.show = this.profiles.length > 0;
        this.hide = !this.show;
      } catch (error) {
        console.error(error);
      }
    },

    changePage(page) {
      this.currentPage = page;
    },

    async view(email) {
      this.$storage.setUniversal("user_email", email);
      this.$router.push("/userprofile");
    },
  },
};
</script>