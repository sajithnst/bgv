
<template>
    <v-container fluid>
        <v-layout column>
            <v-card>
                <v-card-text>
                    <v-flex class="mb-4">
                        <v-avatar size="96" class="mr-4">
                            <v-icon>mdi-account </v-icon>
                        </v-avatar>
                        <v-btn @click="openAvatarPicker">Change Avatar</v-btn>
                    </v-flex>
                    <v-text-field
                        v-model="form.firstName"
                        label="FirstName"></v-text-field>
                    <v-text-field
                        v-model="form.lastName"
                        label="Last Name"></v-text-field>
                    <v-text-field
                        v-model="form.contactEmail"
                        label="Email Address"></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" :loading="loading" @click.native="update">
                        <v-icon left dark>check</v-icon>
                        Save Changes
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-layout>
        <avatar-picker
            v-model="showAvatarPicker"
            :current-avatar="form.avatar"
            @selected="selectAvatar"></avatar-picker>
    </v-container>
</template>
<script>
export default {
    name:"userbanner",
    async mounted(){
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.name=res.data.name
    },
    data:()=>({
        name:"",
        email:"",

    }),
}
</script>