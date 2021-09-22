#このファイルが同じフォルダにあると仮定して
#このプログラムを実行して[正解]と画面に表示する別ファイルを作成してください。
def kansu(ans = ""):
    listA = list(range(2, 500, 3))
    if ans in listA:
        return "正解"

    elif ans == "":
        return

    else:
        return "不正解"

