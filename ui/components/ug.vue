<template>
    <v-container class="personalform">
        <v-form v-model="formValid">
            <h4 class="text-center"> UG Details</h4>
            <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
            <v-text-field label="Registration Number" v-model="ug_regno" :rules="[rules.required,rules.ug_regno]"></v-text-field>
            <v-text-field label="Specialization" v-model="ug_specialization" :rules="[rules.required,rules.ug_specialization]"></v-text-field>
            <v-text-field label="College" v-model="ug_college" :rules="[rules.required,rules.ug_college]"></v-text-field>
            <v-text-field label="Marks in % " v-model="ug_marks" :rules="[rules.required,rules.percents]"></v-text-field>
            <v-text-field label="Year of completion" v-model="ug_passout" :rules="[rules.required,rules.ug_passout]"></v-text-field>
            <v-text-field label="University" v-model="ug_university" :rules="[rules.required,rules.ug_university]"></v-text-field>
            <v-file-input @change="fileselect" label="Upload File" :rules="[rules.required]"></v-file-input>
            <v-container class="text-center">
                <v-btn text  @click="submit()" :disabled="!formValid" class="button" color="indigo lighten-2"> Submit </v-btn>
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
        ug_regno : "",
        email : "",
        fail:null,
        name : "",
        ug_specialization : "",
        ug_college:"",
        ug_marks:"",
        ug_passout: "",
        ug_university:"",
        formValid:null,
        rules : {
            required: (v) => !!v || "Required",
            percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
            email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
            name : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
            ug_regno : (v) => v.match(/^-?\d+$/) || "Register number format is wrong",
            ug_specialization : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            ug_college : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            ug_passout : (v) => v.match(/^\d{4}$/) || "Only in Numbers",
            ug_university : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
        },
    }),
    methods:{
        async fileselect(event){
      this.file=event
    },
        async submit(){
            let url="http://127.0.0.1:8000/ug"
            let udata={
                ug_regno : this.ug_regno,
                email : this.email,
                name : this.name,
                ug_specialization : this.ug_specialization,
                ug_college : this.ug_college,
                ug_marks : this.ug_marks,
                ug_passout : this.ug_passout,
                ug_university : this.ug_university
            }
            let result = await this.$axios.post(url,udata);
            console.log(result.data)
            let formdata = new FormData()
            formdata.append('email',this.email)
            formdata.append('ug_regno',this.ug_regno)
            formdata.append('file',this.file)
            let furl="http://127.0.0.1:8000/uploadugpdf"
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
