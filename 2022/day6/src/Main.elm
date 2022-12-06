module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Events exposing (..)
import Set exposing (..)


main : Html msg
main =
    div []
        [ input
            |> decodePuzzleInput
            |> findFirstMarker 4 4
            |> String.fromInt
            |> (++) "Score 1: "
            |> text
        , br [] []
        , input
            |> decodePuzzleInput
            |> findFirstMarker 14 14
            |> String.fromInt
            |> (++) "Score 2: "
            |> text
        ]


decodePuzzleInput : String -> List Char
decodePuzzleInput puzzleInput =
    puzzleInput
        |> String.toList


findFirstMarker : Int -> Int -> List comparable -> Int
findFirstMarker sequenceSize marker datastream =
    let
        countUniqueCharacters =
            if sequenceSize <= List.length datastream then
                List.take sequenceSize datastream
                    |> Set.fromList
                    |> Set.size

            else
                0
    in
    if countUniqueCharacters == sequenceSize then
        marker

    else
        List.drop 1 datastream
            |> findFirstMarker sequenceSize (marker + 1)


inputTest : String
inputTest =
    "bvwbjplbgvbhsrlpgdmjqwftvncz"


input : String
input =
    "cbhbmmqnmmqvqfqgqcqmmtvvvdsvscvssmfmhfmhhgdgcclhlnnvmnvmnnwngnqggqlqhhbqbfbvffcpfcfpcpmcppsgssvcvmmdwmwsmwswnwvnvvtgvgfgqqnlltgllpplhpllrnrwrtrzrlrzllpnlpnplnlwnnzfztzcchczctcbbpwpbbfhhqllgrllnnghnnlnznzzlqqmggqbgbjjlnlnjllwlnwnjnbjnnhhcddgmdmqmllfjllddmgmpggtvvqqwmmhcmmjpjdpdqqnhhqbhhscstsvttbwtwdtwwjffvccrwrvvnqqtwwhgwhwthwthhvshsfsjstshthqqdfdhdqhqrqggfffvhffhbbwtbtvtwvvwgvvjjjvtjvvlmlmtmztmthmhttjwwmqqjffhvhqvvrddbsbfbgffmcfffqqfzzgmggzvggbjjmccftcftfnttqqjzjdzdrrgvgsgvvlqvlqqlplnnjccjqcjcgjgfjgjlgjjzhhjbbbfdbfddgccncppsbbjjsttcqtqgqpqllqggtsthhtvvtrttbthtnhhddvnnbggmtggcsgcscmmvmllttjbjggbzbttrfttgsstwtftdthdththbttcggdldtdlttbvvpgpjpwpwvwcwjwsjsttznztzftzzjpzzrtzrztrrtsrrdtrdtdbdhhdgdwwnjnnvjvsjjrwjjvrrzvrvllrgghgbbgbsssslqlrllbjbttzfztzpzzvtvccszsddtqttjllqgqgpqphptpwttwtmtltljjfnnzwzmzlzssghssqhhphbhfftwwqmwmzzqtzqzqrrndrrmrqrzrszzrcrbccglgcgwgrgdggtvtpptgtfgflglgrrnvrvhrrhlrhhfchfhdhzzwggvbbgfgrrpdrdccfllqflfmlfmlmbbhnbbsblbzbgbqqjppcddcvvsddjfjjlnnwbbflfzzmlmddjssjffcqffwdfdqqphpnhppbttjfjzzdvdjvvddnfffmjfmfmpfmmmdlmlrrhqqcpcmclmmbmppzczjjmlltqlqzzqgqcggdmdzznnnnsjjvbjjwbwhbhfhvvtmmsfmmcgmcmwcwhwnhhpccmbmdbmbgbjbggqqccfllfqqmqwwzbblffthhdnncqnccqppldlpldpllzmmsqqdffnggqlqtllwlglnlnhlhflfssvzzrllbtbnbgnnfvfllwslszswsnnpwwppvspsmmnfnpffrmrhmmctttrjrbjrjpjtpjpssdwdtwtmmtgtsgttlwttfrfvvpjpcjccmtthhldhllzslshhnrnvvfddnllltclcrrhnnjwwwpfpddmtmsmfflslrlmlmwmllgfgmfgmmjttpcpspslsjspsqstqsqqpsprphrrpqqfzqqwcwcddsjjpvvfnfvnnnrncnwcwczzcwzwnwmwffbdfbdfdjjhrhvhhvwvsvhshnhwwzlwlnnphhtjjmljjqzjjsjgsjshhwjjmttvgvsgstggrcrmmrqrhrqrzrmzmggqvqtqgtqqqqltqqwggmmzggjccgmgwgqqmnqnrnprptrrvfrvffnmnfmmnnnwzzldlvlgvlvqqpnphpgglhlshlhzzpcptpssblqvdbpbbcrngctqgptccwpdcpbcjwdmcrzmhwffgzqmmqwpqvplwzmjlzmvmzmbtqjnhzrpppnpntvmjbzmvhjvbgflmmjnwssvqvbnbddfcwqdtvpvddctmpptcjmvwszhbsttcbjlfjvwlljhlqlvvsnzphdjhfswltdhzprltzcszrgcmnmfznmbccstjvjngwpbsfqssfwvpdhhmlmzttzlszsgpvvbcfvzrlsttlqpnqhwtbqfjnbztnwfnhlhfltgdtsrrwrfhlssvsgzpffnnrhgcvclqnjgfhhzswllvcjffpngcmtjphwnbdfrrgjfrfqbnvbwgccsjvvmjgcvqvtggnvgvgnnchbblqnvvdgjtvdmfrzvhvhzcbqzdslphjjqtcwjqptstvvpqgdbgbcmmchjpvjhvbwtlmlnqpldfcbmwvrmpqcsfdhmmwnbvmpglcfbnsgjmljcwpzpwffcqfrbdrztzhqzhzpcrjfdmrctttdrzlmzcqwjftngwjmgqscftnpbjwqrcvqwbwbdhbhvrdcvgrvctjgwjtmdgzwgvdbmsrjpsbhwcqlqzjnzmgpctlwqhfnbmgsprjcqtfjjvzljqpfqgnvrgnjjlmpqgnzpmpsvzjmtvnfgslldjtjdwlzrvqrbvcpspzpcdnpdjmhcdhsbmthmgjqchqwwsnfjnwgpctlwcdpqpmzqcrptscngqnmhzwjdcqwvdmlzntsfbstbtmmnlsspjbjjdspnslgcnlbfnbhjlzjhrrmdbbwtswqpbpwtzhcnldbsfrvndzvcgzjprcrclhfwbvzgthcglfzqrshgtvbflvnznhmlzdtfnrsltnnppqgrtndbsfqmftdnzmqfwdpcrmssldmrrnzchnqpflgbqzqjjrzlfnptqdwzdhmctfbztmfcmbqcwjmgnwgqzqjctphrrthgvpvppztvpzgzhdszfhlzlcnwmfrlsnvftfrlfvbnlwzctphhpfvszntqcvnfmvmwwhsjlnpfhcpjvrncgmsbprwwllvnsbjfhtbtmcvvpzcvqrrqdvgzvllvcvnvvbftngqcqcvvbsqfshmnhwptcsbsnjzltqzmflftrhblqszrzsbfcpgzncvwhlqlcbmgjdpfcmlgdfphsfcgqccthmlzjbdwpsbddwwrtwmsvqwbzwhzmghhrspvbptznqsqvhgnhlwqjnhgnzprrtjddwtqfsshjrvlglhdlstghftmllvzmmfglnscnrtgcwwwzjphzhvqlctdwjlqvbsvlgzrdpvjhhcthgjhlwsgfzlschhfprfcrzfrzmnlwvqsnqlllczwfhswchrlggqszwrvpldrffnzrffbhtfbslgcdrqpjcrbqsrgfrhttcptncfndcbsdbjsqjvgbmnmhlnbltdcgbmllpgjmgljvglrwmrvgthhhzrsmzvgwcfgvcsbzpjcqnhrzhznzjcjghhwqvllrmsvlpzlssrdsqwvzvqwsvfsjqvbgrfbmfzlchqsjgncbljtvzsfdnvmfzcbrlnnvvmjbmgjmqzjtdzpljdwqtvwsrlbslwfvlgbtnmlpcwmngncnmdhqctshmjmnhpqcqzhvlbvgptctrvggdgnpnrlnngrfhsqdfthvcnpwjfjnslcqlfrfvhnctmsqgnqmgpwtlzhtdqhqqrcllzjccnszsqvrzhcffvnfnstgdmljdrqrndljdnfbbjvmpqdnqhtdlnzcvnfjlvzmfzrndhtglvngmbrdbpbnhvfmrbcwqzttnjplgrhchjtfjwfbjfbmzlrnllhzccpfhfhnjpfvzlpbqnhwmpssvwtzhdbtnbtllhpfdcqjjnzgbdrfjjbcltnzdrmtmsmvpjtmdnqszgbqncsvhjbgwswhmghpvstrqbglgrtgbchttbznvvdhppzwnttpgcbdjdhlsqhhtlphjjrjncrmfdtjhdwmjgmpngnbptzwgwdztmhtpglnftwpnnmrmcwfhwnhlsbwsrjnlmdlmffbzsnhsvnbldwtrrhdhfsjdrsnzlgtfzcwwqrfhtrmjhmphqndwtbpczvmfgczmdlqjqdlwmvjjzwmqnpvwzmtjwtprlnbvjdhpjgndrwzcfthnwhnhqpwtcjlhrhdplzsncfmszmhjmgljhnlsrrfwplclcvjjqmtpnwbtsbwdnjdlqntvdnfgwbpwspssprbffjdlcvbwcqlttnwnhwdspfsjhppbhspnrvrsfmzvbwwtjfzmnzwgqddbmcjzzqhqlgrglsvgsjdwlnsbtmqgsnfwwqrjsbcgdlmbgqwvgpqllqwbcplfjrgnzsdtdtvqnrbcrqjhdtqqplvszvtlflgbpwnpzczbvhzfjrslcwcswsgfvvsswzzwhtfjfpsrvcfnrs"
