<template>
    <h1 class="text-center">Incoming Requests</h1>
</template>
<script>
export default{
    name: "Incoming Requests",
    async mounted(){
        this.company_mail = await this.$storage.getUniversal('hrmail');
        let hrurl = "http://127.0.0.1:8000/hr"
        let result = await this.$axios.get(hrurl, { params :{ email : this.company_mail}})
        console.log(result.data)
        let url="http://127.0.0.1:8000/inbox";
        let res=await this.$axios.get(url);
        this.mail= res.data;
        console.log(this.mail);
    },
    data:()=>({
        mail:[],
        company_mail:"",
        name : "",
    }),
}
</script>