def exist(board, word):
    m = len(board)
    n = len(board[0])
    s = ""
    count = 0
    visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
    for i in xrange(m):
        for j in xrange(n):
            if helper(board,i,j,count,s,word,visited):
                return True
    return False

def helper(board,m,n,count,s,word,visited):
    if count == len(word):
        return True

    if m < 0 or n < 0 or m > len(board)-1 or n > len(board[0])-1:
        return False

    if visited[m][n]:
        return False
    ret = False
    if board[m][n] == word[count]:
        visited[m][n] = True
        ret = helper(board,m+1,n,count+1,s+board[m][n],word,visited) or \
        helper(board,m-1,n,count+1,s+board[m][n],word,visited) or \
        helper(board,m,n+1,count+1,s+board[m][n],word,visited) or \
        helper(board,m,n-1,count+1,s+board[m][n],word,visited)
    visited[m][n] = False
    return ret

if __name__ == '__main__':
    print exist(["a"],"b")
    print exist(["CAA","AAA","BCD"], "AAB")
    print exist(["ab"],"ba")
    print exist(["aa"],"aaa")
    print exist(["aaaa","aaaa","aaaa"],"aaaaaaaaaaaa")
    print exist(["pfhnuvuzzpujstpivosmqlctynsputylyiaufutfjnqdjfnevftotvhticjevjrvrrpxl","kewzubibppwwikpdulnwusrdjoxbdwopalowoxxdotcwgrzaeowygpesddvizjzbwnxlm","uqanswtmxvqorruixonajvbvuctkzgwtxzirxedxzwltphbmwpmhmncjpwvqctjbsttsx","ypxwcqljtxfklpxarirpdhuwsxpmqjjryinaabluytekidkblerolnnekeqdnbulkjnkk","ygltlxbqhdclwszjfftjvwwysjkeyxqxdbqqyuhixlvvduelbzwwytxqehwdenckquarq","jznuwiatonuojtmeqejzbogqsqimszdcysyvdaqrnkhxdtdtyovbcbtwrbjlbonbioynq","ohezodciiyixvlbweypfjagxqihegvuvcawsfacoyklvvmrbkghthnsxxcdexzbbcxthx","wxyiitgxnhjtqfcgxbdbejygmbilxrjvpjfzelwtvinlnrtmtxoziofvqngnfrkwcpvhd","scycplpjhbcepbmehhwwqldhvzkkvtnpvnrnbgwijyozbcfkmbhcmkjjmvthojykyrzbx","vjivzjycojorqqfcbooxixltvxrowtntewqefpgwywnqotuphjmriakgzcuyxitbekflz","nhzjvpzqlpxwdpffbnfdhfarycxijjjzqiknzkdlzdhesoktbpzlubcufadrloqbzarak","unlxxqrlanproanpehvemmpbetcekcrgqegnwxaympparcqwmnaybsbfndlxgcfwjllfj","levdvwuyoqmbtkclmjaruxxxeviqinbutwxpurpkkdndnrqbaqtvpsutqcjyrksnjrefl","vsvyfanxspxikuzeouusgtmqnzbffjqabnygpnfhcfrozqtokniqiujwvmbavtayiahxo","mesrvjrnchxrrqambwjnzklsmjcpszfffxycgrrkaqesgeghcpvbbivqrxfmykrfjrhsj","aejqidxmjgqbbreloufnzrllisxbbpkbtwscbpqnvhozaskpnpcoiqcqizskoeljcfleu","crslhtlbfaqxfffvhyfgsrwwffbktfhxybifutgbwxybeeyleftwxrucyvorcvoayyfss","ouqlutparcewxcvqxxouogxjwxivfcptyfgvyxvrbcpyelobkeyykvkjuuezytuxaauax","ptytiyytobetzefuoopksqjnlipncpntilntmlocmuvozdiprzamsjbfrrstifmttbmfm","ahbxfpwizlbblptwrynkqisyxnrybynehobodxyekafypyuiykspsnpragqegdintleyi","ccucisuinchxvyrinjktzobeyqxjuvtxxobhgvqvyxuvxmfkvpfwggaewzotuhqtxrben","tbnswkpipzfggbmmdtkchdwqtrqnuwcnxphtzwdqxiwdjjrmccolfmdbgtqapsqpjxikw","matuwzghqslujycvefbzvernugyrqinekjziihsazdviexgicjjznaohimzzwodgxeqhl","iknofvsedcinnjaoxkyjlxfbdnbjdixoskczhwflapanycdvmcgzblbgacqgknufxyggu","orudrjcunzirgiutjbultcxgwefullqzfmewvgskgbdojyhuzdfsfeabjfxuspvxbzwzi","olqrpecnnwordgwiiarpznhpkhsldtvtfnlurnjhmxypfuznwscwhlnrshfvbapiocchp","nodmovrlughnifutsooatjdvallcptucjzoyuhjpnsexyyssogujsxfuiqxxltbxsrxny","ienaimaihtxnnghllcvebvrwwooqldqtjewrswazrzpffwstapxbkqxjfozstpodvkwog","ypaxefddzydoxhbngkuwjnqybvwlrktsbtpgaulbsqqpxrdedxammsmnniahuwbwpqesl","rtdhlvfealhzlvmgibvscenyflpwphjgdonojuvlfcltyxziyuaczpagaqcrzlzccptlj","oxpskkshjahfbkgsmntcrkcfkghzzukntzgdlymwzwccikwuzpxrabwmhflhzxwvxcykd","nhejjirvelvukmwnkivrvessanrfocibjmkuudpyomsbyookyldtrwmujfzxhjysvkopn","epeskftavdzjhsafgwomvoveoobzesmiisdsxwuvzteiognudeiysgfgwghabwljoodmk","zhjtnuhtjdwnoxhucqqkxqntbwkpbwzbflwuhfnqikgwjpqnfgxfzlaajksnitqpeojnt","xgbjmaubqhjzeqyrqadbusloibuwkirjosucsoflvokcektxmyahqlvamryzbpkpiftcv","znrpzvwjqtypvfhgcivtgwxwgogniijjwcyxxwhprhemmmtquqlcmiysxeifprqnvokun","rjeyormcmeyeqaqabkxhsewlujgluaynkeoavcejhcnzedzhqxpidnwazcltflirpyrnb","xwkzmjfrknhjesnropqqalvnuoeufrxcqhdcsltdybmctbvjqmzsxxhtlmqtdnxvxdxro","tuowjsrmnafzzxzyhumtmhyaguzltqzmnpiwhzkvzpwbpxbwunrgwpidjhodyqrlfajpz","vkbliecgfaavririrwuynzyfqjmqubsqlvdwzhcgjebcmvkdtgegfclyoaqibkapfflgo","nnxtobflmjfunlarzyfzqqcbsrgacnoraokqpqcdbhyquahvanwqfzrxsaxvnoopczhrr","lxsuvkpxrmxglpnkhlchkzwyonanuuggraaokrndgkkrzxbikfrvfnvvaykxuqdnqfbaz","odfapybpbmbgdynruktsuqmkvzcdcecskjubhxqkjusnsigmszgnqsznteqxispsdlumj","mwsgphzxnnrpugfogsikjhudznhkjvtvsocjvdglqzakghzmzjykqsqrhzcquxmmlqvjt","dujduwjbvxcgxpyrfqzgspardpdtkooqiyteuehrdlzaaxrhnqnhiqbnfgjruxhexciti","rmlcllfjfmyxcihujvzpeqjbanbcxulojysumxfrmeoqmwkvtjmxbvabkdgjatzjrrddp","jwbnnrblbyemkbphdtthzchubqnsvrjepktcdwngwruiukpadkheoqypilkdetkugdylc","muyfohcyycbjlhxbfpjtbmxuytccsqggkenynpzmtaxeiufplqimfgjdbnhtdnbpupohg","nvapsezpmraeznjhypjlwermiggzwpfllhbdmcsatvevkqcifnvdumpcvxbrnifyqgdek","ygetmzfcdnjrknnzcpwcsnpaupscswnsetlruqtxfdqssdrwunymcppxehzzgorkhfbbv","xbdarxuvoqpdrehgtglaimiwdteiuhgriltaipxygodzukfntsqbeyxktdsqnahvldxts","wtalwzhjhvczndgncqjgizvjiqwlosgmlixkkhtrevsraygcopkzqfkzyimmasymdywnh","relmweoxkqncdmskytihgwhaxvdxtqekwpyvvosfhfjkueuuxfbdbleaijxeadqyuptpd","nvmvgwpktlkapnbctekdbofhfdbwzrbmoohumyhhkrhzgldapnfsekzlpbjoumdickepl","lwxeeylrbngqsaucahtdqixdlhfxlwkxvhbbfosibaztavxadrfvbeymlglxewuzfxcnm","uvpuwjxsixvzfqajrovzcsfyohfnjsbgqrcmazeixbkesmnldimfcrfsykgifhovyshas","mlrpvvjjiumtirxayqajwiofylersgjgrawoxfyfckakeymcqnnoxdtwozpjgapxcnmzt","mgxwjhcjufzjsngyicmitvqvnnzabavnjsmscobytchopnoxschnyxjnnknqlleudsmhg","pfcrosicghwipjiouvbfluqwykbsylynsaghuolavhlmqtbnreseyicyufquqrjjtpsof","doakbpcvqpowjuxtwvpbojufudyjvmqadtkeiobagrwpltlhralhkfmgkmqhzihebtkjj","ojrfihtduawundgupneefndnwjpptabhmspubizvkwsybystnzxsocillzcezdonwdjzl","jvvhnvknqdbpavdefopgrwiwmvspfscqpzzevjrlnucpsfuxwjephmltjgkoamgpmftjp","muchwtzdnybzeqgsecckmskzzbneuwvgszpototipvhtnqorsqdekpdlqsqkontgniwgz","sqonyjcozwipzmcpsnhkfsztnhiveqwwgmleypuxlepnrrelenvmfwfugnskdoijbvqbm","myarnpkgtvngszopgkvtchyrrjuobxaovahlprrkoetgfjxltugwdgpwqlktilhflqqdj","knxoggwpfhlcojfuycmlogvzpangtqrdfrtoxpfexqgnzmjzqwkeehgtivbbnvgsmzglp","opoewbgkkfaisgobokjjnmwisruuxfjnvxutaadmhfxbnldcvonjdkrxboravcosbilbk","qqrvnvjyynuoafrmwppmgqijgakqooceevcrqnrqalfcswppnedwwlfeorwefyilukckx","udzhicagtrwzusyixeyqbcybmjvzoiyilarvetdxkzyhryrqdrjgvhhhqdienjoajixnb","ammckvvjmmodxuyebhwgsbtbrvkzszdtlpxxmsiagwfdsdjumgcejyhattcosfjfwgdiy","nkhmpkeuuagafnjdwlyqnmiuvqqdtacikjubvbvrberirclnqmffyoaweszzvdjhoejmh","edikxtbzerrswxtmzpsrqtowdwmjhyqncaybtbcauustrnhsealxvatayhlhgdukeslzw","nbqjwjcjruotglqigrinepvijhoeunairstncwyvsoqabgihzsxehuotccxwrzgiraxvy","yqqmgropbxouuubpiwrktpcuwmmykjwiaowifkxjiodeigtrdmbycftashyeqwoskkdsv","abfogjzmfqprrovzjxrqvvitjbgveysgbxxhjwtomlhfbdekaxcysktdnzbrztaarxhcv","dqjqxorcvddshdnrwsfwtyxnaygxhiumydcxstapyfhfiwzgpgcigaxhadghnbwneylyu","nnssxactzikfntnpsupwbylcuzivmhpzwjttjvpkfzrsufhnzylczwetxpojwfkupfoaa","fliecazhkojizlhvsdvjtefzrbqwrqzwbhbghcptqacrmjogojpiqwjhxzdppentlozvs","qokrsbfcqlsbcarajyzieoaietwsurnkhxdabietvwuzzmzimztqptbtoxoiqduxcazdi","dygctfbhhjtgemxxntnkjxcmsbqsbucguiinqjuxvqfzcczrxmdikfuegnyhhcqblyrdk"], "afdfghjhy")