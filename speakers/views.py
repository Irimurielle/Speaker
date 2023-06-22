from django.shortcuts import render

# Create your views here.

speakers = [
    {
        "id": 1,
        "name": "Olatunbosun Tijani",
        "profession": "Entrepreneur",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/51/Bosun_Tijani.jpg",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 2,
        "name": "Burna Boy",
        "profession": "Singer",
        "image": "https://yt3.googleusercontent.com/P6SjTt-BXjTWeUcpBX-dDUcLhpCboucwr6PN0cpvR3Z7BNq7V0-CmUbVPjGbWyB33ZaO9APa=s900-c-k-c0x00ffffff-no-rj",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 3,
        "name": "Paul Kagame",
        "profession": "President",
        "image": "https://www.paulkagame.com/wp-content/uploads/2021/10/Speech-2-500x450.jpeg",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 4,
        "name": "Bill gates",
        "profession": "Philanthropist",
        "image": "https://cdn.vanguardngr.com/wp-content/uploads/2020/05/Bill-Gates.jpg",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 5,
        "name": "Alexandra Mary Hirschi",
        "profession": "Presenter",
        "image": "https://qph.cf2.quoracdn.net/main-qimg-2fbfe2b6521b177ca9fae8ffeb609839-lq",
        "bio": "Lorem ipsum dolor sit amet",
    },
    {
        "id": 6,
        "name": "SSSniperWolf",
        "profession": "Youtuber",
        "image": "https://nationaltoday.com/wp-content/uploads/2022/09/11-SSSniperWolf-Birthday-1200x834.jpg",
        "bio": "Lorem ipsum dolor sit amet",
    },
]


def speakers_list(request):
    return render(request, "speakers_list.html", {"speakers": speakers})


def speaker_detail(request, pk: int):
    speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
    return render(request, "speaker_detail.html", {"speaker": speaker})


def speaker_update(request, pk: int):
    speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
    return render(request, "speaker_update.html", {"speaker": speaker})

def speaker_delete(request, pk: int):
    speaker = list(filter(lambda speaker: speaker["id"] == pk, speakers))[0]
    return render(request, "speaker_delete.html", {"speaker": speaker})