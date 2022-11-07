<template>
    <v-app exp>
        <v-container>
            <v-form v-model="isFormValid">
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
                </v-col>
            </v-form>
        </v-container>
    </v-app>
</template>
<script>
export default{
    name :'expdata',
    data : () => ({
        email : '',
        name :'',
        empid:'',
        company:'',
        hr_mail: '',
        start_date: '',
        end_date: '',
        designation: '',
        lpa : '',
        reporting_manger: '',
        rules: {
            required : (v) => !!v || "Required",
        }

    })
}
</script>