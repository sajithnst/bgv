<template>
  <v-container>
    <br>
    <v-row>
      <v-col cols="4">
        <personalupload/>
      </v-col>
      <v-col cols="4">
        <sslcupload/>
      </v-col>
      <v-col cols="4">
        <hseupload/>
      </v-col>
    </v-row>
    <v-row>
      
      <v-col cols="4">
        <ugupload/>
      </v-col>
      <v-col cols="4">
        <pgupload/>
      </v-col >
      <v-col cols="4">
        <expupload/>
      </v-col>
    </v-row>
   
<br><br>
  </v-container>
</template>
<script>
export default{
    layout:"hr_layout",

}
</script>