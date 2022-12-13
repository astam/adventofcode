module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import List exposing (..)
import Set exposing (..)


main : Html msg
main =
    div [ style "font-family" "Courier New, Courier, monospace" ]
        ([ input
            |> decodePuzzleInput
            |> cycleInput
            |> aggregateInput 0 1
            |> getEvery40
            |> getSum
            |> String.fromInt
            |> (++) "Score 1: "
            |> text
         , br [] []
         , text "Score 2: "
         , br [] []
         ]
            ++ (input
                    |> decodePuzzleInput
                    |> cycleInput
                    |> aggregateInput 0 1
                    |> drawPixel
                    |> drawScreen
                    |> showDisplay
               )
         -- ++ (inputTest2
         --         |> decodePuzzleInput
         --         |> cycleInput
         --         |> aggregateInput 0 1
         --         |> drawPixel
         --         |> splitToLines
         --         |> showDisplay
         --    )
        )



-- showPixels: List (Int, Int, String ) -> List (Html msg)
-- showPixels pixels =


showDisplay : List a -> List (Html msg)
showDisplay lines =
    case lines of
        [] ->
            []

        x :: xs ->
            text (Debug.toString x) :: br [] [] :: showDisplay xs


decodePuzzleInput : String -> List (List String)
decodePuzzleInput puzzleInput =
    puzzleInput
        |> String.split "\n"
        |> List.map (String.split " ")


cycleInput : List (List String) -> List Int
cycleInput program =
    case program of
        [] ->
            []

        x :: xs ->
            case x of
                [ "noop" ] ->
                    -- let
                    --     _ =
                    --         Debug.log "noop: " 0
                    -- in
                    0 :: cycleInput xs

                [ "addx", y ] ->
                    let
                        value =
                            String.toInt y |> Maybe.withDefault 0

                        -- _ =
                        --     Debug.log "addx: " value
                    in
                    0 :: value :: cycleInput xs

                _ ->
                    []


aggregateInput : Int -> Int -> List Int -> List ( Int, Int, Int )
aggregateInput index total values =
    case values of
        [] ->
            []

        x :: xs ->
            ( index + 1, total * (index + 1), total ) :: aggregateInput (index + 1) (total + x) xs


getEvery40 : List ( Int, Int, Int ) -> List ( Int, Int, Int )
getEvery40 aggregates =
    aggregates
        |> List.filter
            (\( x, _, _ ) ->
                modBy 40 (x + 20) == 0
            )


drawPixel : List ( Int, Int, Int ) -> List ( Int, Int, String )
drawPixel aggregates =
    aggregates
        |> List.map
            (\( cycle, _, sprite ) ->
                let
                    position =
                        modBy 40 cycle - 1
                in
                if (position >= (sprite - 1)) && (position <= (sprite + 1)) then
                    ( position, sprite, "#" )

                else
                    ( position, sprite, "." )
             -- if (modBy 40 cycle >= (sprite - 1)) && (modBy 40 cycle <= (sprite + 1)) then
             --     ( modBy 40 cycle, sprite, "#" )
             -- else
             --     ( modBy 40 cycle, sprite, "." )
            )


splitToLines : List a -> List (List a)
splitToLines pixels =
    if List.length pixels > 40 then
        List.take 40 pixels :: splitToLines (List.drop 40 pixels)

    else
        [ pixels ]


drawScreen : List ( a, b, String ) -> List String
drawScreen pixels =
    let
        screen =
            pixels
                |> List.map
                    (\( _, _, x ) ->
                        x
                    )
                |> splitToLines
                |> List.map (String.join "")
    in
    screen


getSum : List ( Int, Int, Int ) -> Int
getSum every40 =
    every40
        |> List.map
            (\( _, x, _ ) ->
                x
            )
        |> List.sum


inputTest1 : String
inputTest1 =
    """noop
addx 3
addx -5"""


inputTest2 : String
inputTest2 =
    """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


input : String
input =
    """addx 2
addx 3
addx 1
noop
addx 4
noop
noop
noop
addx 5
noop
addx 1
addx 4
addx -2
addx 3
addx 5
addx -1
addx 5
addx 3
addx -2
addx 4
noop
noop
noop
addx -27
addx -5
addx 2
addx -7
addx 3
addx 7
addx 5
addx 2
addx 5
noop
noop
addx -2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx -29
addx 30
addx -26
addx -10
noop
addx 5
noop
addx 18
addx -13
noop
noop
addx 5
noop
noop
addx 5
noop
noop
noop
addx 1
addx 2
addx 7
noop
noop
addx 3
noop
addx 2
addx 3
noop
addx -37
noop
addx 16
addx -12
addx 29
addx -16
addx -10
addx 5
addx 2
addx -11
addx 11
addx 3
addx 5
addx 2
addx 2
addx -1
addx 2
addx 5
addx 2
noop
noop
noop
addx -37
noop
addx 17
addx -10
addx -2
noop
addx 7
addx 3
noop
addx 2
addx -10
addx 22
addx -9
addx 5
addx 2
addx -5
addx 6
addx 2
addx 5
addx 2
addx -28
addx -7
noop
noop
addx 1
addx 4
addx 17
addx -12
noop
noop
noop
noop
addx 5
addx 6
noop
addx -1
addx -17
addx 18
noop
addx 5
noop
noop
noop
addx 5
addx 4
addx -2
noop
noop
noop
noop
noop"""
