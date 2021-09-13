import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            if len(stack) == 0:
                return "NO"
            if c == ")":
                prev = stack.pop()
                if prev != "(":
                    return "NO"
            elif c == "}":
                prev = stack.pop()
                if prev != "{":
                    return "NO"
            elif c == "]":
                prev = stack.pop()
                if prev != "[":
                    return "NO"

    return "YES" if len(stack) == 0 else "NO"


if __name__ == "__main__":
    # print(isBalanced("{[()]}"))
    # print(isBalanced("{[(])}"))

    tests = '''[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]
[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}
(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]
){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]
}(]}){
((]()(]([({]}({[)){}}[}({[{])(]{()[]}}{)}}]]{({)[}{(
{}{({{}})}[][{{}}]{}{}(){{}[]}{}([[][{}]]())
(){}[()[][]]{}(())()[[([])][()]{}{}(({}[]()))()[()[{()}]][]]
()([]({}[]){}){}{()}[]{}[]()(()([[]]()))()()()[]()(){{}}()({[{}][]}[[{{}({({({})})})}]])
[]([{][][)(])}()([}[}(})}])}))]](}{}})[]({{}}))[])(}}[[{]{}]()[(][])}({]{}[[))[[}[}{(]})()){{(]]){][
{()({}[[{}]]()(){[{{}{[[{}]{}((({[]}{}()[])))]((()()))}(()[[[]]])((()[[](({([])()}))[]]))}]})}
()(){{}}[()()]{}{}
{}()([[]])({}){({[][[][[()]]{{}[[]()]}]})}[](())((())[{{}}])
{}(((){}){[]{{()()}}()})[]{{()}{(){()(){}}}}{()}({()(()({}{}()((()((([])){[][{()}{}]})))))})
][[{)())))}[)}}}}[{){}()]([][]){{{{{[)}]]{([{)()][({}[){]({{
{{}(
{[{((({}{({({()})()})[]({()[[][][]]}){}}))){}}]}{}{({((){{}[][]{}[][]{}}[{}])(())}[][])}
()[[][()[]][]()](([[[(){()[[]](([]))}]]]))
()[]({}{})(()){{{}}()()}({[]()}())[](){}(({()}[{}[{({{}}){({}){({})((({()})))}}}]]))
}[{){({}({)})]([}{[}}{[(([])[(}){[]])([]]}(]]]]{][
[{]{[{(){[}{}(([(]}])(){[[}(]){(})))}}{{)}}{}][({(}))]}({)
)})[(]{][[())]{[]{{}}[)[)}[]){}](}({](}}}[}{({()]]
[[[({[]}({[][[[[][[{(()[][])}()[][]][]{}]]]]}))][(()){}]]]()[{}([]{}){}{{}}]
({[]({[]})}())[][{}[{{(({{{([{}])}}}))}}]]
([((()))()])[][][]{}()(([]))[]()[]((){}[]){}(){{}[]}[[{[]}]]
[[(((({}{[]{}()}){}{{}}){({[]{[{}]{(){}(((){()}))}()}}[[]]()()[()])[[{}{}]()]}))]]{}[]{}({({{}})})
(]{()}((
[][(())[({{{()[]}}{[[][[][[[]{{{[()]{{{{}{[]}[][]}}}}}}]]]]}})]]
}[})})}[)]{}{)
({(}{})))}(}[)[}{)}}[)[{][{(}{{}]({}{[(})[{[({{[}{(]]})}
]}})[]))]{][])[}(])]({[]}[]([)
[{{}{[{{[}[[}([]
[([]){}][({})({[(([])[][])][[{}{([{{}{(()){{{({}{{}}())}}[]}}()[()[{{{([](()){[[[]]]})}}}]]}])}]]})]
]{}{(}))}](})[{]]()(]([}]([}][}{]{[])}{{{]([][()){{})[{({{{[}{}](]}}
{[{}}){(}[][)(}[}][)({[[{]}[(()[}}){}{)([)]}(()))]{)(}}}][
(]{}{(}}}[)[
[]{}{[[]]}([{}]{}[]){{(())}}
[)([{(][(){)[)}{)]]}}([((][[}}(]{}]]}]][(({{{))[[){}{]][))[]{]][)[{{}{()]){)])))){{{[(]}[}}{}]
{({(){[[[][]{}[[([]{})]{}]][[]()()]]}})}[{}{{}}]
)}][(})){))[{}[}
{[]{({]}[}}[{([([)([){{}{(}}[]}}[[{[}[[()(])[}[]
()()()[]
((){}])][]][}{]{)]]}][{]}[)(])[}[({(
)[((])(]]]]((]){{{{())]}]}(}{([}(({}]])[[{){[}]{{}})[){(
}][[{[((}{[]){}}[[[)({[)}]]}(]]{[)[]}{}(){}}][{()]))})]][(((}}
([]){}{{}{}}()([([{}{[[]()([(([]()))()[[]]])]}])])
[()[[]{{[]}()([])}[]][][]][]()[]{}{}[][]{}{}[()(){}]
{[{){]({(((({](]{([])([{{([])[}(){(]](]{[{[]}}())[){})}))[{})))[
{}[()[]][]{}{}[[{{[[({})]()[[()]]]}}]]
{[{}[][]]}[((()))][]({})[]{}{()}
(){[{({})}]}
([]])][{)]({)[]))}]())[}]))][}{(}}})){]}]{[)}(][})[[
((({{}(([{}(())]))[()]{[[[]()]]}})))
}()))}(}]]{{})}][{](]][{]{[[]]]}]]}([)({([))[[(]}])}[}(([{)[)]]([[](]}]}{]{{})[]){]}{])(
{}{}{}{[[()]][]}
)]}]({{})[[[{]{{{}}][))]{{
))){({}])}])}}]{)()(}(]}([
([[]][])[[]()][]()(([[]]{[()[]{[][{}]}[()]]{}{[]}}{{}()}(()[([][]{})[[{}][]]{}[]])))
(]{[({}[){)))}]{[{}][({[({[]))}[}]}{()(([]{]()}})}[]{[)](((]]])([]}}]){)(([]]}[[}[
([[]])({}(([(){{}[{}]}]){[{}]}))[][{}{}](){}
[][][][][][([])][]{({()}[[()()]{([(){[]{}}{(())}{[](){}()({}())}[({}[[]()])][]])}])}
}[{{(}})}}(((())()({]{([]((][(({)[({[]]}[])}]{][{{}]{)][}(])}}}))}}}
[]({})()[]{}{}[]({}{})[]{([])()[()][{()({})[{}{[[()]{}[]][]}(({{[]{()()()}{}[]()}[]}){{}{}})]}]}
{{(([{)]{}({][{](){({([[[][)}[)})(
[{}]{[()({[{}]})]}
[[{}]]
]{{({[{]}[[)]]}{}))}{){({]]}{]([)({{[]){)]{}){){}()})(]]{{])(])[]}][[()()}
{[([}[[{{(]]][}()())]{){(){)]]){})}]{][][(}[]())[}[)})})[][{[)[})()][]))}[[}
]()])}[}}}{]]{)[}(}]]])])}{(}{([{]({)]}])(})[{}[)]])]}[]{{)){}{()}]}((}}{({])[}])[]}
(]}[{}{{][}))){{{([)([[])([]{[
{(()[]){}}(){[]}({{}(()())})([]){}{}(())()[()]{}()
{{}[{}[{}[]]]}{}({{[]}})[[(){}][]]{}(([]{[][]()()}{{{()()}{[]}({}[]{()})}{()}[[]][()]}))
{[][]}[{}[](){}]{{}{[][{}]}}
()(){}(){((){}[])([[]]())}
{}[[{[((}[(}[[]{{]([(}]][[
{}[([{[{{}()}]{}}([[{}[]]({}{{()}[][][]})])])]
{[](}([)(])[]]})()]){[({]}{{{)({}(][{{[}}(]{
[][]{{}[](())}{}({[()]}())[][[][({}([{}]))]]
((()))[]{[(()({[()({[]}{})]}))]}{[]}{{({}{})[{}{}]{()([()])[{()}()[[]{}()]{}{}[]()]}[[]{[]}([])]}}'''.splitlines()
    expects = '''YES
YES
NO
NO
NO
NO
YES
YES
YES
NO
YES
YES
YES
YES
NO
NO
YES
YES
YES
NO
NO
NO
YES
YES
YES
YES
NO
YES
NO
NO
NO
NO
YES
NO
NO
NO
YES
NO
YES
NO
NO
YES
NO
NO
NO
YES
YES
NO
YES
YES
YES
NO
YES
NO
YES
NO
NO
YES
NO
YES
YES
NO
YES
NO
YES
YES
NO
NO
NO
NO
YES
YES
YES
YES
NO
YES
NO
YES
YES'''.splitlines()
    out = []
    for item in tests:
        out.append(isBalanced(item))

    for i in range(len(out)):
        if out[i].strip() != expects[i].strip():
            print(f"{i} {out[i]} {expects[i]}")
