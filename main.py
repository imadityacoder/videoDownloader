from pytube import YouTube,Playlist
from time import sleep
from flet import (
    Page,
    app,
    Text,
    TextField,
    colors,
    Row,
    Dropdown,
    dropdown,
    IconButton,
    KeyboardType,
    ThemeMode,
    icons,
    Icon,
    Banner,
    AppView,
    NavigationBar,
    NavigationDestination,
    AppBar,
    FilledButton,
    alignment,
    Padding
)


def main(page:Page):
    page.title="Welcome to Aditya's Youtube-Video-Downloader"
    page.vertical_alignment = alignment.top_center
    page.padding = Padding(top=100,right=0,bottom=0,left=0)
    page.horizontal_alignment = "center" 
    page.theme_mode= ThemeMode.LIGHT   
    page.bgcolor = colors.PURPLE_100
    page.navigation_bar = NavigationBar(destinations=[
            NavigationDestination(icon=icons.VIDEO_FILE, label="Download Video"),
            NavigationDestination(icon=icons.VIDEO_LIBRARY, label="Download Playlist"),
            
        ]
    )
    page.appbar = AppBar(
        leading=Icon(icons.APPS_OUTAGE_SHARP),
        leading_width=30,
        title=Text("Aditya's Downtube App"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
    )

    boxh = 80
    boxw = 400
    fsize = 20

    urltext = Text(
        value="Enter your URL here:",
        size=17,

        )
    
    page.update()    

    urlbox= TextField(
        text_size= fsize,
        border_radius= 8,
        height=boxh,
        width=boxw,
        opacity=0.9,
        bgcolor=colors.PURPLE_50,
        border_color="black",
        hint_text="https://www.youtube.com/watch?v=Vds8ddYXYZY"
    )
    btndown= FilledButton(
        text="download now",
        icon=icons.DOWNLOADING_ROUNDED,
        opacity=0.8,
        width=boxw-24,
        height=boxh-40,
        )


    page.add(
        Row(
            [
                urltext,  
            ],
            alignment="center",
        ),
        Row(
            [
                urlbox,
            ],
            alignment="center",
        ),
        Row(
            [
                btndown,
            ],
            alignment="center",
        ),

    )
    
    page.update()

if __name__=="__main__":

    app(target=main,view=AppView.FLET_APP_WEB)