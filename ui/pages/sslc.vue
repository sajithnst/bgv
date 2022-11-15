<template>
    <v-app sslc>
    <v-container class="sslcform">
        <v-form v-model="isFormValid">
            <v-alert type="error" v-model="fail"> Data Insertion Failed</v-alert>
            <h1 class="form-title text-center"> SSLC Details</h1><br/>
            <v-divider></v-divider><br/>
            <v-col>
                <v-row>
                    <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Marks in % " v-model="marks" :rules="[rules.required,rules.marksmax]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="School Name" v-model="school" :rules="[rules.required,rules.nospecchar]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Year of Completion" v-model="passout" :rules="[rules.required]"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field label="Board" v-model="board" :rules="[rules.required, rules.nospecchar]"></v-text-field>
                </v-row>
                <v-row>
                    <v-file-input @change="fileselect"  label = "Upload SSLC Certificate as PDF" :rules="[rules.required]">
                    </v-file-input>
                </v-row>
                <v-row>
                    <v-btn large block color="teal" @click="save()" :disabled="!isFormValid"> Save </v-btn>
                </v-row>
            </v-col>
        </v-form>
    </v-container>
</v-app>
</template>
<script>
   export default {
    name : "sslcdata",
    async mounted(){

        let url ='http://52.27.5.60:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));
    },
    data : () =>({
        isFormValid : null,
        email :'',
        name : '',
        regno :'',
        marks :0,
        school :'',
        file:null,
        passout :'',
        fail:null,
        board :'',
        rules:{
            required: (v) => !!v || "Required",
            marksmax :(v) => v< 100 || "The maximum marks is 100",
            nospecchar: (v) => v.match(/^[A-Za-z ]+$/) || "No special Characters allowed",

        }


    }),
    methods:{
        async fileselect(event){
            this.file=event
        },
        async  save(){
            let fdata= {
                email : this.email,
                name : this.name,
                regno : this.regno,
                marks : this.marks,
                school : this.school,
                passout : this.passout,
                board : this.board,
            }
             let url = 'http://52.27.5.60:8000/sslc'
            await this.$axios.post(url,fdata).then(res => {
                if (res.data == true){
                    this.$router.push('/hse')
                }else {
                    this.fail = true
                }
            }).catch( err => { console.log(err)})
            let formdata= new FormData()
            formdata.append('email',this.email)
            formdata.append('regno',this.regno)
            formdata.append('file',this.file)
             let furl="http://52.27.5.60:8000/uploadsslcpdf"
            await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}}).then(res => { 
                if (res.data == fales){
                    this.fail = true
                }
            }
            ).catch( err => { console.log(err)})
        

        },
    }
   }
</script>
<style>
.sslcform{
    width: 40%;
    margin: 5% auto;
}
</style>