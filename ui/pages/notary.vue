<template>
  <v-app notary>
    <v-app-bar app>
       <v-btn icon><v-icon>mdi-home</v-icon></v-btn>
       <v-spacer></v-spacer>
       <V-btn icon><v-icon>mdi-logout</v-icon></V-btn>
    </v-app-bar>
    <v-main>
      <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-system-bar
      color="indigo darken-2"
      dark
    >
      <v-spacer></v-spacer>

      <v-icon>mdi-window-minimize</v-icon>

      <v-icon>mdi-window-maximize</v-icon>

      <v-icon>mdi-close</v-icon>
    </v-system-bar>

    <v-toolbar
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Discover</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="item in items"
          :key="item.id"

        >
          <v-card>
            <h1 class="text-center">{{item.subject}}</h1>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>

              <v-btn icon>
                <v-icon>mdi-bookmark</v-icon>
              </v-btn>

              <v-btn icon>
                <v-icon>mdi-share-variant</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
    </v-main>
    
  </v-app>

</template>
<script>
export default{
    name :"mailmodel",
    async mounted(){
        let url = "http://127.0.0.1:8000/inbox"
        let res=await this.$axios.get(url)
        console.log(res.data.value);
        let items = res.data.value;
        console.log(items[0].id)
    },
    data:() =>({
      items: [],
      cards: [
        { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
    
}
</script>