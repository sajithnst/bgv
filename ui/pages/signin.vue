<template>
    <v-app signin>
        <v-app-bar>
            <v-btn icon ><v-icon size="32">mdi-home</v-icon></v-btn>
        </v-app-bar>
        <v-main>
            <v-container>
                <v-form>
                    <v-col>
                        <v-row>
                            <v-text-field label="Email ID"></v-text-field>
                        </v-row>
                        <v-row>
                            <v-text-field label="Password"></v-text-field>
                        </v-row>
                        <v-row>
                            <v-btn large block color="teal" @click="signin()"> Sign In</v-btn>
                        </v-row>
                    </v-col>
                </v-form>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name : 'signinpage',
    data: () =>({
        signin : {
            username : '',
            password : '',
            
        }
    }),
}
</script>