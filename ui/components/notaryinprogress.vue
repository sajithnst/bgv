<template>

  <v-container>
    <v-container v-if="show">
      <v-list>
      <v-list-item 
      v-for="request in paginatedRequests" 
      :key="request.email">
      <v-list-item-title v-text="request.name"></v-list-item-title>
      <v-list-item-subtitle v-text="request.email"></v-list-item-subtitle>
      <v-btn icon @click="view(request.email)"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
      </v-list-item>
    </v-list>
    <v-container class="text-center">
      <v-pagination v-model="currentPage" :total-visible="5" :length="totalPages" @input="changePage"></v-pagination>

    </v-container>
    </v-container>
    <v-container v-if="hide">
      <h2 class="text-center" style ="color:darkblue"> No Profiles</h2>
      
    </v-container>
  
  </v-container>
    
</template>

<script>
export default {
  name:"notaryinprogress",
data() {
  return {
    currentPage: 1,
    paginatedRequests: [], 
    requests:{},
    show:false,
    hide:false,
  };
},
async mounted(){
  this.$vuetify.theme.dark=false;
        let url = "http://127.0.0.1:8000/inprogressuser"
        let res = await this.$axios.get(url)
        this.paginatedRequests = res.data.list
        this.requests = res.data.count

        if(this.paginatedRequests==false){
          this.hide=true
          this.show=false
        }

        else{
          this.hide=false
          this.show=true
        }
},
computed: {
  totalPages() {
    return Math.ceil(this.requests.length / 10);
  },
  paginatedRequests() {
    const startIndex = (this.currentPage - 1) * 10;
    const endIndex = startIndex + 10;
    return this.requests.slice(startIndex, endIndex);
  },
},
methods: {
  changePage(page) {
    this.currentPage = page;
  },


  async view(email){
    this.$storage.setUniversal('user_email', email)
    this.$router.push("/userprofile")
  }
},
};
</script>