<template>
    <v-container  class="personalform">
        <v-form >
            <h4 class="text-center"> HSE Details</h4>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
            <v-text-field label="Marks in Percents" v-model="marks" :rules="[rules.required,rules.percents]"></v-text-field>
            <v-text-field label="Year of Completion" v-model="passout" :rules="[rules.required]" ></v-text-field>
            <v-text-field label="School" v-model="school" :rules="[rules.required]"></v-text-field>
            <v-text-field label="Board" v-model="board" :rules="[rules.required]"></v-text-field>
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
        regno : null,
        marks : null,
        email: null,
        passout: null,
        school : null,
        fail: null,
        school : null,
        board : null,
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
            let url= "http://127.0.0.1:8000/hse"
            let hdata = {
                regno : this.regno,
                email : this.email,
                name : this.name,
                marks: this.marks,
                passout: this.passout,
                school: this.school,
                board : this.board

            }
            let result = await this.$axios.post(url,hdata);
            let formdata = new FormData()
            formdata.append('email',this.email)
            formdata.append('regno',this.regno)
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
