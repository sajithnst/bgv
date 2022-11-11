<template>
    <v-app exp>
    <v-app-bar app>
    <v-spacer></v-spacer>
    <v-btn text @click="addnewexp()">Add Experience</v-btn>
    <v-btn text @click="finishexp()">Finish</v-btn>
    </v-app-bar>
    <v-main>
        <v-container class="expform">
            <v-alert type="success" v-model="success" > The Experience added for {{empid}}</v-alert>
            <v-form v-model="isFormValid">
                <h1 class= "text-center"> Experience Details</h1><br/>
                <h3 class="text-center"> Enter the data again to save multiple exprience details</h3><br/>
                <v-col>
                    <v-row>
                        <v-text-field label="Employee ID" v-model="empid" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Start Date (DD.MM.YYYY)" v-model="start_date" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="End Date (DD.MM.YYYY)" v-model="end_date" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Company Name" v-model="company" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Designation" v-model="designation" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="CTC" v-model="lpa" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="Reporting Manager" v-model="reporting_manger" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-text-field label="HR Email" v-model="hr_mail" :rules="[rules.required]"></v-text-field>
                    </v-row>
                    <v-row>
                        <v-file-input @change="fileselect()"  label = "Upload Experience Certificate as PDF" :rules="[rules.required]">
                        </v-file-input>
                    </v-row>
                    <v-row>
                        <v-btn large block color="teal" @click="save()">Save Experience Details</v-btn>
                    </v-row>
                </v-col>
            </v-form>
        </v-container>
    </v-main>
    </v-app>
</template>
<script>
export default{
    name :'expdata',
    async mounted(){
        let url ='http://192.168.26.93:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));
        
    },
    data : () => ({
        email : '',
        name :'',
        empid:'',
        company:'',
        hr_mail: '',
        start_date: '',
        end_date: '',
        success: null,
        designation: '',
        lpa : '',
        reporting_manger: '',
        rules: {
            required : (v) => !!v || "Required",
            dateformat : (v) => v.match(/[0-9]{2}.[0-9]{2}.[0-9]{4}/) || "Date format is wrong",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
        },

    }),
    methods:{
        async fileselect(event){
            this.file =event
        },
        async save(){
            let edata = {
                empid : this.empid,
                email : this.email,
                name : this.name,
                company : this.company,
                hr_mail : this.hr_mail,
                start_date : this.start_date,
                end_date : this.end_date,
                designation : this.designation,
                lpa : this.lpa,
                reporting_manager : this.reporting_manager,

            }
            let url ="http://192.168.26.93:8000/exp"
            await this.$axios.post(url, edata).then(res =>{
                if (res.data == true){
                    this.success = true
                }else{

                }
            }).catch(err => {
                console.log(err)
            })
        },
        async addnewexp(){
            this.$router.push('/exp.vue')
        },
        async finishexp(){
            this.$router.push('/signin')
        },
    }
}
</script>
<style>
.expform{
    width: 40%;
    margin: 0% auto;
}
</style>