<template>
    <v-app ug>
        <v-container class ="ugform">
            <v-alert type = "error"  v-model = "fail">Data insertion Failed</v-alert>
            <v-form v-model="isFormValid">
                <h1 class="form-title text-center">  Undergradute Details </h1><br/>
                <v-divider></v-divider><br/>
                <v-col>
                    <v-row>
                        <v-text-field label="Registration Number" v-model="regno" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Marks in percentage" v-model="marks" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="College" v-model="college" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Specialization" v-model="specialization" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Year of Completion" v-model="passout" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="University" v-model="university" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-file-input @change="fileselect()"  label = "Upload UG Certificate as PDF" :rules="[rules.required]">
                        </v-file-input>
                    </v-row>
                    <v-row>
                        <v-btn large block @click="save()" color="teal"> Save UG Certificate</v-btn>
                    </v-row>
                </v-col>
            </v-form>
        </v-container>
    </v-app>
</template>
<script>
export default {
    name:"ugdata",
    async mounted(){
        this.email = await this.$storage.getUniversal('Email');
        let url ='http://127.0.0.1:8000/user'
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));

    },
    data:() =>({
        isFormValid:null,
        email:'',
        name : '',
        regno :'',
        file :null,
        marks :0,
        college :'',
        specialization :'',
        passout :'',
        university :'',
        file:null,
        fail:null,
        rules:{
            required:(v)=> !!v || "Required",
        }

    }),
    methods:{
        async fileselect(event){
            this.file =event
        },
        async  save(){
            let ugdata= {
                regno : this.regno,
                name : this.name,
                email : this.email,
                marks : this.marks,
                college : this.college,
                specialization : this.specialization,
                passout : this.passout,
                university : this.university,
            }
            let url = 'http://127.0.0.1:8000/ug'
            await this.$axios.post(url, ugdata).then(res => {
                if (res.data == true){
                    this.$router.push('/exp')
                }else{
                    this.fail = true
                }
            }).catch(err => {
                console.log(err)
            });
            let furl ='http://127.0.0.1:8000/uploadugpdf'
            let formdata = new FormData();
            formdata.append('email', this.email)
            formdata.append('regno', this.regno)
            formdata,append('file',this.file)
            await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json'}}).then(res => { 
                    if (res.data == false){
                        this.fail = true
                    }
                }
                ).catch( err => { console.log(err)})
        },
    }
}
</script>
<style>
.ugform{
    width: 40%;
    margin: 5% auto;
}
</style>