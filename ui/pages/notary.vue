<template>
 <v-app notary>
    <v-app-bar app>
      <v-btn icon @click="home()"><v-icon size="32">mdi-home</v-icon></v-btn>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout()"><v-icon size="32">mdi-logout</v-icon></v-btn>
    </v-app-bar>
    <v-main>
        <v-row>
          <v-col>
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
                        <v-btn icon @click="sendmail(mail.from.emailAddress.email)"><v-icon icon>mdi-email</v-icon></v-btn> &nbsp;
                        <v-btn icon><v-icon icon>mdi-delete-circle</v-icon></v-btn>
                      </v-list-item>
                  </v-list-item-group>
                </v-list>
            </v-container>
          </v-col>
          <v-col>
              <v-container class="sm-auto">
                <h2>Outgoing Requests</h2><br/>
                  <v-list
                  style="max-height:500px"
                  class="overflow-y-auto">
                    <v-list-item-group>
                      <v-list-item v-for="exp in exps" :key="exp.empid">
                          <v-list-item-content>
                            <v-list-item-title v-text="exp.name"></v-list-item-title>
                            <v-list-item-title v-text="exp.company"></v-list-item-title>
                          </v-list-item-content>
                          <v-btn icon><v-icon >mdi-email</v-icon></v-btn>
                          <v-btn icon><v-icon>mdi-delete-circle</v-icon></v-btn>
                      </v-list-item>
                    </v-list-item-group>
                </v-list>
              </v-container>
          </v-col>
        </v-row>
      
       
  
    </v-main>
 </v-app>
</template>
<script>
export default{
    name :"mailmodel",
    async mounted(){
      let url = "http://127.0.0.1:8000/inbox"
      let res=await this.$axios.get(url)
      this.mails = res.data;
      console.log(this.mails)
      let eurl = "http://127.0.0.1:8000/pendingexp";
      let eres = await this.$axios.get(eurl)
      this.exps = eres.data
    },
    data:() =>({
      mails: [],
      exps:[],

    }),
    
}
</script>
