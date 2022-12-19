<template>
 <v-container class="sm-auto">
              <h2> Incoming Requests</h2><br/>
              <v-list 
              style="max-height: 500px"
              class="overflow-y-auto"
              >
                  <v-list-item-group >
                      <v-list-item v-for="mail in mails" :key="mail.id">
                        <v-list-item-content>
                          <v-list-item-title v-text="mail.from.emailAddress.name"></v-list-item-title>
                          <v-list-item-title v-text="mail.subject"></v-list-item-title>
                        </v-list-item-content>
                        <v-btn icon @click="sendmail(mail.id,mail.from.emailAddress.address)"><v-icon icon>mdi-email</v-icon></v-btn> &nbsp;
                        <v-btn icon @click="discard(mail.id)"><v-icon icon>mdi-delete-circle</v-icon></v-btn>
                      </v-list-item>
                  </v-list-item-group>
                </v-list>
            </v-container>
</template>
<script>
export default{
    name : "incoming",
    async mounted(){
        let url = "http://127.0.0.1:8000/inbox"
      let res=await this.$axios.get(url)
      this.mails = res.data;
    },
    data: () =>({
        mails:[],
    }),
    methods:{
      async sendmail(id,email){
        console.log(id, email)
        let mailurl = "http://127.0.0.1:8000/sendprofile"
        let mail={
          id: this.id,
          email: this.email
        }
        let res=await this.$axios.post(mailurl,mail)
        console.log(res.data)
      },
      async discard(id){
        console.log(id)
      }
    }
}
</script>