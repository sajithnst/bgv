<template>
    <v-card>
      <v-card-text class="text-center">
        <v-btn  color="indigo darken-4" style="color:white; width:90%;" @click="showForm = true">Add Address</v-btn>
      </v-card-text>
  
      <v-dialog v-model="showForm" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">Address Form</span>
          </v-card-title>
  
          <v-card-text>
            <v-form ref="form" v-model="valid">
              <v-text-field v-model="houseNo" label="House No" :rules="[rules.required,rules.houseNo]"></v-text-field>
              <v-text-field v-model="street" label="Street" ></v-text-field>
              <v-text-field v-model="region" label="Region" ></v-text-field>
              <v-text-field v-model="state" label="State" ></v-text-field>
              <v-text-field v-model="country" label="Country" ></v-text-field>
              <v-text-field v-model="zipcode" label="ZIP Code" ></v-text-field>
            </v-form>
          </v-card-text>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" text @click="showForm = false">Cancel</v-btn>
            <v-btn color="primary" :disabled="!valid" @click="submitForm()">Submit</v-btn>
          </v-card-actions>

        </v-card>
      </v-dialog>
    </v-card>
  </template>
  
  <script>
  export default {
    name:"Addaddress",
    async mounted(){
      this.email = this.$storage.getUniversal('Email');
    },
    data() {
      return {
        showForm: false,
        valid: false,
        email:"",
        houseNo: "",
        street: "",
        region: "",
        state: "",
        country: "",
        zipcode: "",
        rules: {
          required:(v) => !!v || 'House No is required',
          houseNo: (v) => /^\d+$/.test(v) || 'House No must be a number',

          },
      };
    },
    methods: {
      async submitForm() {
        let url="http://127.0.0.1:8000/personal/address";
        let pdata={
          email: this.email,
          houseNo: this.houseNo,
          street: this.street,
          region: this.region,
          state: this.state,
          country: this.country,
          zipcode: this.zipcode,

        }
        let result = await this.$axios.post(url,pdata)
        if(result.data == true){
          this.$router.push('/')
        }
        else{
          this.fail=true;
        }
        },
      },
    };

  </script>
  