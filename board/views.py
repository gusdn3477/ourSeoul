from django.shortcuts import render
from .models import Board
from .forms import BoardForm
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator

# Create your views here.
def board_list(request):

    all_boards = Board.objects.all().order_by('-id')
    # 변수명을 all_boards로 바꿔주었다.
    page = int(request.GET.get('p',1))
    # p라는 값으로 받을거고, 없으면 첫 번째 페이지로
    pagenator = Paginator(all_boards, 2)
    # Paginator 함수를 적용하는데, 첫 번째 인자는 위에 변수인 전체 오브젝트, 2번째 인자는
    # 한 페이지당 오브젝트 2개씩 나오게 설정
    boards = pagenator.get_page(page)
    
    return render(request, 'board/board_list.html', {"boards":boards})

def board_write(request):

    if not request.session.get('user'):
        return redirect('/accounts/login/')

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            # 이 부분에 session 처리 예정
            user_id = request.session.get('user')
            member = BoardMember(objects.get(pk=user_id))

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            # 검증에 성공한 값들은 사전타입으로 제공(form.cleaned_data)
            # 검증에 실패시 form.error에 오류 정보를 저장
            board.writer = member
            board.save()

            return redirect('/board/list/')

        else:
            form = BoardForm()

    return render(request, 'board/board_write.html', {'form' : form})

def board_detail(request, pk):

    try:
        board = Board.objects.get(pk=pk)
    # pk에 해당하는 글을 가지고 올 수 있게 된다.

    except Board.DoesnotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html')
    # {'board':board}로 템플릿에 전달해 준다.