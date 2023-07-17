<template>
  <v-container class="personalform">
      <v-form>
          <h4 class="text-center"> PG Details</h4>
          <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
          <v-text-field label="Registration Number" v-model="pg_regno" :rules="[rules.required,rules.pg_regno]"></v-text-field>
          <v-text-field label="Specialization" v-model="pg_specialization" :rules="[rules.required,rules.pg_specialization]"></v-text-field>
          <v-text-field label="College" v-model="pg_college" :rules="[rules.required,rules.pg_college]"></v-text-field>
          <v-text-field label="Marks in percent (e.g. 80)" v-model="pg_marks" :rules="[rules.required,rules.percents]"></v-text-field>
          <v-text-field label="Year of completion" v-model="pg_passout" :rules="[rules.required,rules.pg_passout]"></v-text-field>
          <v-text-field label="University" v-model="pg_university" :rules="[rules.required,rules.pg_university]"></v-text-field>
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
      pg_regno : '',
      email : '',
      fail:null,
      name : '',
      pg_specialization : '',
      pg_college:'',
      pg_marks:'',
      pg_passout: '',
      pg_university:'',
      rules : {
        required: (v) => !!v || "Required",
          percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
          email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
          name : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
          pg_regno : (v) => v.match(/^[a-zA-Z0-9]+$/) || "Register number format is wrong",
          pg_specialization : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
          pg_college : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
          pg_passout : (v) => v.match(/^\d{4}$/) || "Only in Numbers",
          pg_university : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
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
        
          let url="http://127.0.0.1:8000/pgupdate"
          let udata={
              pg_regno : this.pg_regno,
              email : this.email,
              name : this.name,
              pg_specialization : this.pg_specialization,
              pg_college : this.pg_college,
              pg_marks : this.pg_marks,
              pg_passout : this.pg_passout,
              pg_university : this.pg_university
          }
          let result = await this.$axios.post(url,udata);
          console.log(result.data)
          let formdata = new FormData()
          formdata.append('email',this.email)
          formdata.append('pg_regno',this.pg_regno)
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
