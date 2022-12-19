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
            <incomingmail/>
          </v-col>
          <v-col>
              <outgoing/>
          </v-col>
        </v-row>
      
       
  
    </v-main>
 </v-app>
</template>
<script>
export default{
    name :"mailmodel",
    data:() =>({
    }),
    
}
</script>
