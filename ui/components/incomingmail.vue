<template>
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
                        <v-btn icon @click="discard(mail.id,mail.from.emailAddress.address)"><v-icon icon>mdi-delete-circle</v-icon></v-btn>
                      </v-list-item>
                  </v-list-item-group>
                </v-list>
</template>
<script>
export default{
    name : "incoming",
    async mounted(){
        let url = "http://127.0.0.1:8000/inbox"
      let res=await this.$axios.get(url)
      console.log(res.data)
      this.mails = res.data;
    },
    data: () =>({
        mails:[],
    }),
    methods:{
      async sendmail(id,email){
        let mailurl = "http://127.0.0.1:8000/sendprofile"
        let mail={
          id: id,
          email:email
        }
        console.log(mail);
        let res=await this.$axios.post(mailurl,mail)
        console.log(res.data)
        window.location.reload()
      },
      async discard(id,email){
          let url = "http://127.0.0.1:8000/deletemail"
          let pdata = { id : id , email : email}
          let res=await this.$axios.post(url,pdata)
          console.log(res.data)
          window.location.reload()
      }
    }
}
</script>