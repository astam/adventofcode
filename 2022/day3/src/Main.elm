module Main exposing (..)

import Debug exposing (..)
import Html exposing (..)


main : Html msg
main =
    div []
        [ input
            |> decodeRucksack
            |> findDuplicate2
            |> calculateScore
            |> String.fromInt
            |> (++) "Score 1: "
            |> text
        , br [] []
        , input
            |> decodeGroups
            |> findDuplicate3
            |> calculateScore
            |> String.fromInt
            |> (++) "Score 2: "
            |> text
        ]


decodeRucksack : String -> List ( List Char, List Char )
decodeRucksack puzzleInput =
    puzzleInput
        |> String.split "\n"
        |> List.map
            (\x ->
                let
                    begin1 =
                        0

                    eind2 =
                        String.length x

                    eind1 =
                        eind2 // 2

                    begin2 =
                        eind1
                in
                ( String.toList (String.slice begin1 eind1 x)
                , String.toList (String.slice begin2 eind2 x)
                )
            )


findDuplicate2 : List ( List a, List a ) -> List (Maybe a)
findDuplicate2 decodedList =
    decodedList
        |> List.map
            (\( x, y ) ->
                x
                    |> List.filter
                        (\z ->
                            List.member z y
                        )
                    |> List.head
            )


findDuplicate3 : List ( List a, List a, List a ) -> List (Maybe a)
findDuplicate3 decodedList =
    decodedList
        |> List.map
            (\( x, y, z ) ->
                x
                    |> List.filter
                        (\a ->
                            List.member a y && List.member a z
                        )
                    |> List.head
            )


decodeGroups : String -> List ( List Char, List Char, List Char )
decodeGroups puzzleInput =
    puzzleInput
        |> String.split "\n"
        |> combineGroups
        |> List.map
            (\( x, y, z ) ->
                ( String.toList x
                , String.toList y
                , String.toList z
                )
            )


combineGroups : List String -> List ( String, String, String )
combineGroups decodedGroups =
    case decodedGroups of
        [] ->
            []

        x :: y :: z :: xs ->
            ( x, y, z ) :: combineGroups xs

        [ _ ] ->
            []

        [ _, _ ] ->
            []


calculateScore duplicates =
    duplicates
        |> List.map
            (\x ->
                case x of
                    Just y ->
                        let
                            code =
                                Char.toCode y
                        in
                        if code >= 97 then
                            code - 96

                        else
                            code - 38

                    Nothing ->
                        0
            )
        |> List.sum


inputTest : String
inputTest =
    """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


input : String
input =
    """WVHGHwddqSsNjsjwqVvdwZRCbcJcZTCcsZbLcJJsCZ
hngprFFhFDFhrDpzzQDhtnBJJRJZbZvTcvbfRCJfBRcBJl
DmptngtFwvvMmwmm
HFddrJnLdqtHBMQBmmVm
gbvNsbhsvQtmZTbQPT
vDshDlczcDhcssscwzQwslLJrSJLpqrrzpnCrSfLSnqq
pDGQDSpFDGzFDQSJqzDhjhQMTjTrwTstbTBTjTtLtbTMBT
zgzVNHHgMwMLbLNB
WRWPgdHCZccggJmJGzJmzGhGCD
sVJNlhldShpdpnnwVnwCwtwggt
WLFFcHWQLPPZQCgtnCgmbtbHwt
MPLWzRMMcGgRrWNDpSSSfDflMlTd
BBMZJcgBRjCZZzBpSvHQvbLvvHCQLQ
VlVTFwDTVGnfWSQPtsDPbvrpDS
wWdqhWlwGVfGwlfTVqFWfWWjzZZBJmMZMNdzZJMpjzNjgJ
FBWFphQBmDmpmMSpDWVcVcvsPcRbrjPMcMsr
HHtdnHnwNCHCTJRTPTzrbvVbcVRr
lHqHwlnlqnGCNGGmWDvvZfpZvG
mfVtmPtsccMmHcHCFfmhVmnpgZLbWPZqWnpqZbZWpgPW
zzvwBrzdQDvpZJfQJZJpLf
BrTBwRdNcfNmfStc
sTlhFLfZTTLcfsLlLDZflvQvRNqRJFNvRMRNvQQRBQ
CWcgwStWwCWWwvgNQvJBvQMQRB
wptGzbzGWVGSCVVlVlLDcVVsfhLTlf
HVnMVGwLLbsGnVsLnwLSBggMhjmgmgmhtmqhtgMhMj
zrZzJRZfzZfrPCrFcWccPdTdHHlvdmlgTghCtmtTgq
NFfcZWWzZrrHLBpBBGVGNG
HqFhhCBCBLmwwCqJCHFvvFdcprrrSSrjRFRjpgrggb
VGzWtQzGGQPVtlVNslVWsPdRpmcRrjpSzcrcbdSmSnSg
WPPGllQMPGmTLvLJBCwM
PvDWRSmTVvSvRhbZRpRpbjjjzM
GBFGHLglHrrrLgGrttbMjpbcpcZJBsBp
lrHgrrndgdNnlHGFQPMMmWPTvvWSCDQn
mmhQShhmhQfzNfTTlShbHJrRtltltJJtHlRLLZ
WscggNqwPWjcGcWWcpNcRJHHprZvZHrvtttZJpJr
jGjgcMGCwPNsGDCcszBfhhQQQDnFnTVVBV
mcGjrwzQcrZtQzZQDZcPssvPVVCPCVLwswwPBC
NJbqHddNSgdPWvvsVHVLPs
NqglNSlJFNSbSNdldNlNdNbTRFDrvRmQrQGtmDrvttQmmtDj
zzcBPnHBjgHjWJvbJQTvScbwcQ
qdspVCFqVqfFqLFCqtpTwtpTbSTbJpwBST
FRLFRCNNqMfdWNmZPBPZrHmm
VmtRRJmtrDrwhRcvPspltvgqtqsd
WGQBZzMMBGBGbZTTWWCMNSgggqnPlsfbqndndccglffg
CWQQZMFWdzMQdJJwJVFrwmmmRw
rZsFfGfNhznzsjhzZfVjGVvVdvSTSJHSDDtcmmmttC
wWpRBWlbWMWlQDvCcRSvJRSStm
LPlwWqbgwqjjcFshNf
lsppsGphmPrRQnvHdRpd
qBgjLqMjgjTLPnzHPrPRLnzv
gSMfNjNtttVbqBbtTSStjTqlhmlZDsDsbWZWFFFsGhlWPm
sPDPDzrGzBsGRsbwrjtSVvthVfQtQw
ClpgFZgNqMWCgqCpMNZqNWmNdtSwtljtVHQhtwfvdHtSdhSj
FpNCJpNcpfCpgNWPGBLcbTGTzTzPnG
mssNLCZqSqmNCHmrqHChJTjTjnRRnnqVnTTGngGTRn
dbwptFwQbvdtcvpZDcDddgzGPjTGgpPTRpzzzgRzTn
BwZdtZldDbrSsNrsrSHl
MLnFWMRWpnpnLnLCmPGTqQsFzBttTQ
SwNlDHNcddglSDBjrqmqGQqqmGtGGwszPP
vdSlNcrvvvnBMbBR
psZPRmTpRpgrlrDRBFgV
jvCqNhwnjhGNqCMqVgFHWtgHBrtwHFrJ
cGvbNcjvvhhjcvbQGcZdZSQpzdpmpPVpdZpd
drTHDdlHzllZDTzTQRQLsPPSsBbSjQdL
MfVVWmNvMnqNmVVpMMgfgMmvBFFfRRLQPPsPfsFLFCFRSFjR
whMnNVnqWmlllHswJTZT
ZSQTTLLlTsbmmDZlmNQSNFfPwHwqCjCCfjwFPwfwLr
MctMJMBVttnhJcBBVctwRHjHRJwJwjFfqPfRwj
vzqgqhBVzzTlZmmTlN
WgvlHJFvljvdBmzcvcwpmchc
TQqZsTZttLZbRZsLLMzzppBmNShCmBNTcNCN
LPMZsMZLMQVgglFPhFHlFl
qsBCPVPqVbwfnMQNmZJnqJgR
hHdrvvLWtvtjWQnZJTMrmpTZgN
DShSShLZdFGPGDPGsPsG
qRBddRzFFqFqHnNnPSnnmmSpgpJm
ssZDQMvvMwppNJWRDRpW
MMvwlsRMcQBjcLqLBBqc
ZGHpwFGvwpHrvfFTMtDfccMjntMntc
RgSCLRLJRSRSQQqJmTDMPMTtsJjnclBjtj
LVmmSSddLCwVHDbzDzZr
psgWdsBjnnJjbZWQDDLNrDcrLVQjLM
zPSCCHqCfqfmWNMcrVSLRM
TPHzWPFTGztqTGgdJdsssvZgwb
gcFgBChcClJjNCPb
sWZdZdrSmWmSZRwSmsvPlsTtTtNMnnlvnJJv
GSWrHZdGQpRrrSGmpWQmQfLfpVzDfghppzBVLBlBqg
BFNqFzBNhqVwmTtsqVst
dMwMwMfCMWbDtDvDssCC
ldMwMSHHMMWJpRpPLLpBzPZjgnZPhN
WczRJhcWggVBdzPPLnCjdvjm
lSpSTpTSsCCmmntNdp
wSFDCTwsGDqQqQVWWcJw
RqPqhDGBhRDrrhBFmPmbgssZbwbgCbwsmZsQ
nCtjMppjfTpjJJfVZwtzZtllLZwLss
MHfpMWdHpSCSfnSTJWhDDFDFBGqDGvvDBDFd
MCCGMCSHVGNTspVWQznddndg
rttLtvRbrhLZrbcQdJnnQdfddsrggf
BbRqltRtHsNNllNC
ncFpcsLLdFmWlRmnllTR
bMMVzVqMzjNVDblmRTPGlSmmPlqG
gNDDJMVZNCbNJNDNQCbZCbscvBsdBvrRHfcpdQpfFFff
VnWFbZvFbHWhFjZWVJZJLZFWTttpMCspQTTzQCHpgQMgztzT
dGcfdNdGrlRlBDGNSllfBMspgzmTgtQQgztMtzpmcT
lBNdqRsBRdfPNrLPFVVPVJPZZvhj
TLWgggJzwjgWgjgGnnmQnzQfNNNQsm
SpPbBlPBMlvFZpbbBmQGsmCJmCstsdNGBQ
MhSHhZPrPbvSFrJPpPMSbMcLjjqTLHDRTDDTTLDLTqgH
fprRRbbznFbcQVPDdQPdFV
LTvmsLmcsHmvDvSZDZVVSS
jWtmLccssJTLjHmLWWJwnwlBfwnBbllpCBnffbBr
plPBWzbnFLPPtGqMMwlMGwmS
ZQjDHjrQjdjVFwdMvCSfmwMqdt
DDhhrRDjQghHJjhWBbgbTccbsTzpWF
vgCbbwsTbWWWgwBWDGGDqtPGtMgGlFMH
znrznJNhLSLphRRRDlFPMmpFPjjHtMFF
llNcSQVSNcRbvCwwWcTdwZ
qpnJbnRRnJhRFhFHRgQSzHlSRHCCCg
fMBttBvsBjffvsQTtfGTWlCWsSgSmHCzZmLlHgzZ
ffMdjrfdwjfwwnhJPFchhqwQ
NCVSTCVCQCCRVDQSJsqFPsPNspFhhsgjPh
btvtWtcWnpgmFhjmmt
cfnffBfcWcrMdbvMQJDDrDTDVCpCDrGD
fZNhBWFSlFQFjWQTTldHgCwvTvqqdr
zznVzCznmHvnwgdH
PMMbCGPMDPcLbJhFhWhBhRScQZBQ
WQMrDWGHbSWHMNrTQRhghmgPZccmqDLwPqPg
svCzfpdzzdsnslCsnPZcHZPlJcqZgmqPPc
nntVpdpVsfjCHzvnsCzRTBrtWGbNNQSMbTNSRr
SnpDQdBqGpDSBMfQGcMQBDJPNstvJcWNsPJCtJtNRWPC
VrVHrhTHlPHTvvNtbhNRNswC
TzlFHHmrVlgTlTGSzGqpdMGBPQBS
zrCDnrDVCnCgnrHgGDnVVCZsNttQZmjtsmbMqGqsjbqj
TlRRWPSwwFwbSwTTTpNQQqNjqZZlmMMQQt
wvbwbRTLWdFFwvRBTbvTTRzrnznnJrDDCzBczBfHCJnz
SvTdmLNNNdvTBmvmLvSvDpgczzjfgjggpcjcNPzD
VJHQsJVlHpjjpzsjzP
VRlJbJQrVbVHJJPMhBdnBRCSLZZZnvnLvv
tMGcpGtMtLtsCGspLzNCBBmwCzQRzBBRWQ
hdlHFllDdZgDbDDlDHTWWTnzBBBvzmNHzwRz
FSddDlFRqDFqFSdPVqdhcfGMsVtVfLjrfGfjtMcs
RGMWnBMWfCCMBHTDptJJgZStRPmSRD
bqzFqjqcFLNLZZSmpSBgZZ
rFrQNbNBlNcbrQlNQvvclMswTCTCnwrwHrWGsGCswn
WLhJQddCQwRNCQNHczHNzMvZcZvcNc
SlSpSlrpDqnbqDjlGjGGljTjMZZPPMMfVPgfHMMVgVvqfgcw
SbGsDspbbnjTjBldCFmLwFCJLBmtJB
TMDjMvMqMvDTzcmFCgrJCr
ZZZJSZWVBHZWSSZQJhVhWnHJwczGGwGcCCFzwgmzcwFgwVzc
pLHNQSnNJsMLRJds
TsLZGwdsDFWHBZJFfZ
mqhRvqrzJRbmzJBFfgHHgWgHrrlH
JvvNhJmvtDdsNTwdLV
wwnSVSmwtbstznwgbzzVMTNpTNWdlCSlSWTffWNCSN
cFvccLGFGvvGHZflnNTpnZpZcB
GPqGDhGGqrDhVRgbnbttPmgs
rzSZJScLrcBLvjvsqMPZvjQl
nnpDqgDqFTgwqHHvMHvvvTvPMM
GnqCGpDqqVhccLmrmSmCRL
tJSTmdfddDTDJCPmbQvQLHvqqqbrbvlP
zWGsjcwwGGcVVjcGWcNjvNjQqrQtNFFQHHrF
RZnRVsswRsGWcwVBZVtBRdDJgCffTgmgfnnCpfTfTM
FnCrzhTrNPrMcnhMTnZZZNPwDPdbDmdDtwjdtjbmQwDt
sBvWrpppvLBsLRVBfHSfbbQmbwSjStDSwSwS
LVRRRJqqlHNlNTChrhMG
WNsfsstMvtMvNNGPZwmZmqZPLWZcww
rDCdDRCDFQjSVLcmZcDq
bBBHqTgBbQlQRCQFbgqdhvshGvTJMnfTtnnThnsN
VwWBTNQcVzDtrgfrtzzt
LLbpShLGvlbCmLjpGSCSCpvFdrgdddcHtrtGgfqHcDHqrd
pmvLmlpmjbLbpljJPBBcTBBQRZBBVJRZ
cVTcVTNvvghNhvggPPgtCVSpSQmzCqZDRCmDZDZS
dGJMWFsFMFWsnlzRlQzlzqpzlZzD
HdLFssFMsJbnbFjqbhPgjNggcrhg
LLVhQCTvRvmWlCppQfQQjPrwszNsfzNz
BZSgncHgnJStJHJgntMWzGsrPqGwsfPfGPwwwZ
bdBdJMBcShWCLbhWVC
vjdpGNGwSNCTwwRbfnWgQMLjQWMnLQ
DcmFPFtHmlcgpqWDnMbDLf
FZJPtcprHtPPHplZHPZclwwGBSZSvSwCwvZzNdwvvw
CdJLJCJPWPWcbtzJtqJzFrQvBhfjBBvjjvdjpFjr
sBRgsZGDNSBBRGDwphrrrThpHpgHvhpQ
DwDsGBDNwGmMNlMlMDSPmztJVCbVCCWqPqJLmW
LSTMgDSRSMHbMDWLHSvDScwtCGqGrjGrcLftqVGtVC
hzJPmlphCGrCwVrJ
zhPNdNnQZBZBhZnNZSgMWMDbMHwWSDWNDH
rcdvvcwvrHrMZBjHSZ
sDtWblgnltsDFlgFqltCCVQTMTgSHVTfSQfSHj
tDtRWFpFbWWWWNNDWsNqWvmzvhzhzGmzjjGvLwJmpc
nFSSnnbhSfgLSSnVjdjfHMgfMzGzmqlNGGmTPlqqTzTNNzlT
pBZsJJvccbBmlWGlNb
cvsssvZwsDwrDdfFgnbDfVbgng
mWRNWNCTdwdCwhCddbWWmhsZVgJQJBVBfsBsJQLQBLJb
qFFlGzFtjjcqzHtFtlRfVfsZfQHVfBHQRHgf
jqGjtcDnGnPzFRlzrnMdWrrCMMddNNWT
MHWCjjGMcHhbhPDLphHQ
nRVJrtgssdLgCppvLQbg
RlVVZNVRJlsstldsBCNlczfjjSZmWTcmGmTSfmSm
RTHqgTgMwgnGTRzqTHCGfdFdfhmBrJrdvbFJMhPB
lNZNNNLttLWJBPBdZBFmdZ
SppscpLVStclNPWtCczqnQQwHTTgCGwq
hSHRCbZRSZhbRZBctnMVjwwtWtwh
GrdFzQrDdJstjcWttwsF
drPJLDPGPvDvzrJPQLdDHpZlwLgRmwCHLpwgSbff
zMSSnCtCdSdCtdfMdHMdtVBDjhWDHBqbTVVBqhbDjr
cPNhFFNRlNDlTBqjlTBG
RvmvRpPNRgwgPvFwhmdCssmCzdMshMmL
tttjgrpTwmCgCwgwrrlrHzbzqqFNzdJqqZnddJwNbh
cQjMjPMBfcLBSjGQBndFnzNdNnhzzNGFbF
sSQPLMfVPBVSfBMvVLSPfHCttDjCDRRtrVVglgpttD
vdTvdpBvcTPdSSvCLrCCDLDCQGDl
sRfnFgmFRMVsnqgRmqzmrrDBDwtHlLHtrLCDGL
qRMVjJgRFnJfMssMsgZScPJpZbPbPPWhBZSp
ZJgNJhGZglMZZFDTPSNqFSqTSb
mwdvwpsjrcjBvpwFrvbHcDqbWHRWDSPWDHSR
CsvpsLLjFzhlLGFZ
sDNQrMrNfrlQjJRgGjbTllHG
ZRhSnWFVSwBtFRBVvVgHgbzjgGTJnngmGmHC
vWZLShhvZLVtSFSLqwVrQdqpcqMDddRNQMdsNP
hQhSQbbwtHzShwhSQPbJRsLwRCjJmDCcvmqCcs
FNdBTBTNMsRqqCjTjL
GNdrdMBVFShhSLSGGL
cZzcCmjjcvdzdWqgWTZgPZgZhh
wSwVGSJFTffgJTNh
FSVpVlBMShzbjzcpvp
qqlblClRbnTvqTmRqlmnTwrdfdwFFNrngfddDBrNtr
PcLcQLMVLGMzHLMchhLcjLFrrNrBfrfFNJtNgJDDBNzt
sSjjGcGQscSVSMjHVMSVPSQsWmCmppZCmtCWbbWTlZTqTl
qWlVJmDJHWJHVJlsdVTdhbFNNgFhwhhhFhwwZg
npjnvQpStCQLvBpPnvtBtBpGSGbzbGDggGNbgwghzZNGGN
jBvLtvjnrtMDmmDRTTrsWc
pmwdwzJtFmmlpFsWwtstJPGgvNgCCLWCvPgNNPQCQv
RfbfTRBnRGQvPNnncc
ZTbPZSDSBfSBVSbbBRbbbtrFdtlFmVsswtFwzdpszw
hVphQcmdcWWprWWhChFQBsfHjDTTBCHlSsTSBgSH
vqBRqqzbqMZPMwSTDjJjlHDllgHZ
PMnMLqtMnntQhWBccthB
vqqvCSvHSSwqvqCddnvQFmNbVjbJVVmGNNVHNNlH
pggrhzWgptWhZsmVlFmgNNVNbj
RzpMLLhhphtzrRrSSbQTBQwSTDBwQM
DSFQDlDFRddDHQHQtFlDVsVMTzrMCLSWZLZffSzLWrfCJz
jjBBvpgmbppBPbMwBBBNbbZWZzzCCTzzZgzWcJccLzWz
bvPwNwmpnBNhPmqpPvnwwNmtRQGQMdQDQlsGVVGhRlGFsl
SfJJwDJgpGdSGJNSTwTVJDRbWWfLtCWCLtRLHWrtbWBf
cQQPnFhjjQlczhqllhszhqsQRWnrbrHdHtbWrBWBbtvvHBrW
qMqqqqzFFmPjmmsFjmzsmhjcDGSZTJgTdpZwZgwSZVpMTNVG
czrcHMcMJtCCPnpFmH
DwGGlvLljGmDRdwLdLjfhtFsssnFVpfttpptsnFPnp
TlRTghTjwTDRTDlZZQgWMMrMJMSZmM
BzdNzNdgNNPfgdNsdQdNvVMLLVQVMcCRCMRmvCGc
zHpplwwZrZlqlWWrpZwqlHhLvqMCRDCGVmLcqGMVvCMmMD
rWrjwWwHplZbwpZtHtJJbgfFTfsNnBbsfbSdTzgB
jPRRppDLDGDTLLggMMjpLTGcrJWHsttJfwnWrMvrJnvnrNfJ
blqbzBdzmhhbQWnsNHtJvfssfd
lhFhzSzzSZVNSlVPgDPCPCGTRcGR
cqWcNWffPftvsvfpqPtZsBzrbmbFddBmbcLbdDHbHz
TJgljTnGgnLBTZbHdBFz
JgSnJwSlgGJRwMtfPtvfwsZQZZtv
hHhPbQPTwsdwdHqtgttjpNfjDt
FFlCmSzRCCmlzzRGCFNvRpvjvtZNZqsRfNRg
mVmsFMGFzJFBwQTMnMQndd
QQVpQGcVdGmspHHLtbqfqfbt
JvZTFDFzJzhFCWCZZDzWPBCJfLbnnwLqttnsHHNPwtbHLwjn
DssTMWvvvGMcQGQGld
sshRHZSZRbSZHhBFBMpMWpFgbbtb
JfjTjmwwTPvfTNPTQlmFFFqqmFMBBqFgFt
vDTvJffQTJjJvPvTNSHRzhCsShRRRDtZHz
NFLsRDNNDNBDlgPPgBglQlzj
HJhdZpfJzlWQjjHw
ffJTppZZqTNlGnNsMG
ZMrWcWwqqvPZMndGdqlnnDLnVT
HpCsshCfpFfHHJDDSlSVQQGGflDQ
zssNzRJFhjNHNNHpJRwbwMMzWWtZPcbBbwbG
HlNHHLHsBDRpHLlsHRlJnMhfWZMRnvCCCnWhZj
wtqSmQqttzSSQdPmmwZhChJjWJjPggCZCfZJ
SSwtTbTQmbtdqmGTTcfqzDLHFsBLDGLNGrsBHFGrLB
FFDvWznMWWMrPnPnWPgsmgQbhJRslHbwHwVVsVHjBsHb
ZtSffffpdLqpSCLfCNqfLqLCjHjHbwhpBwJllHlRVQllphjj
ZcNCtcGSctZScqfNGScLNcczPJFmzmDzGzWnrWFPFWDvrM
DnTPspmTPsTCDQWRZzZzZRCRfCfHfh
BNcqTBcFgbVchVJhVR
dTwdrBrwTSPPWnnmSmsn
pfbbDbHpNBFmQbpNNBSlLtlDStSdSPJLtLJR
ZcszvwgVCZswFzVTRTlTlRLgRJSWJR
jzZvVwFjcjjnwvzwZcjMpqMpbGQbQmhhHhmfHQmh
hTbddhQCtdNmdtwtdhTBbCddRSWscczwcRSWLJzcFJzDsFsR
NflgfPZPcgSLJcWD
lPVNZMMMpZlZZvfrMvpbQHQhtbtqdTQHthrqhd
JlWSStwhWJSRJpJvJBjTwTqcwTsDjsCTCB
dqFzgFZGGQNVmTcCrjrzsBrB
fdgLFQLnPdnqShRMPhlJMpWW
TMPcsPDjdDhsDcDcTTTDvdvghBNFGGtmNrSrgSSBGNtNFg
CVCbJqlRVVWWpRqRQZRWVWJZBtmSFGNmggGmtmmBFbrGMGMt
JRqHVJVCRLZWTjMnfLTPcfLd
TRTZFTTrghrZVhVWdWZpMmbzbdzBmtDpDDzmzB
wcsSSsjfPfGPqQwqsQcfJJCtJGpppCBJzCbzJzCb
sPjflcwljfjfvqNcTZTRhtVWrNrVLnrR
rVLLsmwmCWTmsCTdwQrdTmqWDjDHjNGNPbjDBPNDNsZRDBjH
cFcSvgJvfhfLnShtMJtPHRRvRbBBGBPNBHPbND
hgLcgcLpJSMwzmrmzqQrmp"""
