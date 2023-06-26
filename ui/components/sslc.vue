<template>
    <v-container class="personalform" >
    <v-form v-model="formvalid" >
        <br/>
        <h3 class="text-center"> SSLC Details</h3>
        <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
        <v-alert class="success" dismissible v-if="success"> Data insertion succeeded</v-alert>
        <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
        <v-text-field label="Marks in %" v-model="marks" :rules="[rules.required,rules.percents]"></v-text-field>
        <v-text-field label="School" v-model="school" :rules="[rules.required]"></v-text-field>
        <v-text-field label="Year of Completion" v-model="passout" :rules="[rules.required]"></v-text-field>
        <v-text-field label="Board" v-model="board" :rules="[rules.required]"></v-text-field>
        <v-file-input @change="fileselect"  label = "Upload PDF Files" :rules="[rules.required]" ></v-file-input>
        <v-container class="text-center">
            <v-btn text  @click="submit()" color="indigo lighten-2"> Submit </v-btn>
        </v-container>
    </v-form>
</v-container>
</template>
<script>
export default{
    name: "sslc",
    async mounted(){
        var url ='http://127.0.0.1:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));

    },
    data : () => ({
        formvalid: false,
        regno : null,
        email : null,
        marks : null,
        school : null,
        success: null,
        passout : null,
        name : null,
        fail : null,
        board : null,
        rules : {
            required: (v) => !!v || "Required",
            percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
        },
    }),
    methods:{
        async fileselect(event){
      this.file=event
    },
        async submit(){
            let url ="http://127.0.0.1:8000/sslc"
            let sslcdata = {
                regno : this.regno,
                email : this.email,
                marks : this.marks,
                school : this.school,
                passout : this.passout,
                name : this.name,
                board : this.board
            }
            let result = await this.$axios.post(url,sslcdata);
            console.log(result.data);
            let formdata= new FormData()
            formdata.append('email',this.email)
            formdata.append('regno',this.regno)
            formdata.append('file',this.file)
            let furl = "http://127.0.0.1:8000/uploadsslcpdf"
            let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
            if (res.data === result.data){
                this.$router.push('/user')
            }
            else{
                this.fail =true
            }
        },
    }

}
</script>
