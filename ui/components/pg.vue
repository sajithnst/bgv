<template>
  <v-container class="personalform">
      <v-form>
          <h4 class="text-center"> PG Details</h4>
          <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
          <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
          <v-text-field label="Specialization" v-model="specialization" :rules="[rules.required]"></v-text-field>
          <v-text-field label="College" v-model="college" :rules="[rules.required]"></v-text-field>
          <v-text-field label="Marks in percent (e.g. 80)" v-model="marks" :rules="[rules.required,rules.percents]"></v-text-field>
          <v-text-field label="Year of completion" v-model="passout" :rules="[rules.required]"></v-text-field>
          <v-text-field label="University" v-model="university" :rules="[rules.required]"></v-text-field>
          <v-file-input @change="fileselect" label="Upload PDF File" :rules="[rules.required]"></v-file-input>
          <v-container class="text-center">
              <v-btn text  @click="submit()" color="indigo lighten-2"> Submit </v-btn>
          </v-container>
      </v-form>
  </v-container>
</template>
<script>
export default{
  name: "ug",
  async mounted(){
      var url ='http://127.0.0.1:8000/user'
      this.email= await this.$storage.getUniversal('Email');
      await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
          this.name = res.data.name
      }).catch(error => console.log(error));

  },
  data:() =>({
      regno : null,
      email : null,
      fail:null,
      name : null,
      specialization : null,
      college:null,
      marks:null,
      passout: null,
      university:null,
      rules : {
          required: (v) => !!v || "Required",
          percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100"
      },
  }),
  methods:{
      async fileselect(event){
    this.file=event
  },
      async submit(){
          let url="http://127.0.0.1:8000/pg"
          let udata={
              regno : this.regno,
              email : this.email,
              name : this.name,
              specialization : this.specialization,
              college : this.college,
              marks : this.marks,
              passout : this.passout,
              university : this.university
          }
          let result = await this.$axios.post(url,udata);
          console.log(result.data)
          let formdata = new FormData()
          formdata.append('email',this.email)
          formdata.append('regno',this.regno)
          formdata.append('file',this.file)
          let furl="http://127.0.0.1:8000/uploadpgpdf"
          let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
          if (result.data == res.data){
              this.$router.push('/user')
          }else{
              this.fail= true
          }

      }
  }

}
</script>
