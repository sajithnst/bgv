<template>
  <v-container  class="personalform">
      <v-form >
          <h4 class="text-center"> HSE Details</h4>
          <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
          <v-text-field label="Registration Number" v-model="hse_regno" :rules="[rules.required,rules.hse_regno]"></v-text-field>
          <v-text-field label="Marks in Percents" v-model="hse_marks" :rules="[rules.required,rules.percents]"></v-text-field>
          <v-text-field label="Year of Completion" v-model="hse_passout" :rules="[rules.required,rules.hse_passout]" ></v-text-field>
          <v-text-field label="School" v-model="hse_school" :rules="[rules.required,rules.hse_school]"></v-text-field>
          <v-text-field label="Board" v-model="hse_board" :rules="[rules.required,rules.hse_board]"></v-text-field>
          <v-file-input @change="fileselect"  label = "Upload PDF Files"  :rules="[rules.required]"></v-file-input>
          <v-container class="text-center">
          <v-btn text  @click="submit()" color="indigo lighten-2"> Submit </v-btn>
      </v-container>
      </v-form>
  </v-container>
</template>
<script>
export default{
  name: "hse",
  async mounted(){
      var url ='http://127.0.0.1:8000/user'
      this.email= await this.$storage.getUniversal('Email');
      await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
          this.name = res.data.name
      }).catch(error => console.log(error));

  },
  data:() =>({
      hse_regno : "",
      hse_marks : "",
      email: "",
      hse_passout: '',
      hse_school : '',
      fail: null,
      hse_board : '',
      rules : {
        required: (v) => !!v || "Required",
            percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
            email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
            name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
            hse_regno : (v) => v.match(/^[a-zA-Z0-9]+$/) || "Register number format is wrong",
            hse_passout: (v) => v.match(/^(19[0-9]{2}|20[0-2][0-3])$/) || "Only in Numbers",
            hse_school : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            hse_board : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters"
      },
  }),
  methods:{
      async fileselect(event){
    this.file=event
  },
      async submit(){
        let nurl = "http://127.0.0.1:8000/user/expupdation"
        let ndata={
          'email': this.email
        }
        let nres = await this.$axios.post(nurl, ndata)

          let url= "http://127.0.0.1:8000/hseupdate"
          let hdata = {
              hse_regno : this.hse_regno,
              email : this.email,
              name : this.name,
              hse_marks: this.hse_marks,
              hse_passout: this.hse_passout,
              hse_school: this.hse_school,
              hse_board : this.hse_board,


          }
          let result = await this.$axios.post(url,hdata);
          let formdata = new FormData()
          formdata.append('email',this.email)
          formdata.append('hse_regno',this.hse_regno)
          formdata.append('file',this.file)
          let furl = "http://127.0.0.1:8000/uploadhsepdf"
          let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
          if (result.data === res.data){
              this.$router.push('/user')
          }
          else{
              this.fail = true
          }
      }
  }
}
</script>
