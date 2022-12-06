module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Events exposing (..)


main : Html msg
main =
    div []
        [ input
            |> decodePuzzleInput
            |> moveCrate1
            |> getFirstCrates
            |> (++) "Score 1: "
            |> text
        , br [] []
        , input
            |> decodePuzzleInput
            |> moveCrate2
            |> getFirstCrates
            |> (++) "Score 2: "
            |> text
        ]


decodePuzzleInput : String -> ( List ( Int, Int, Int ), Array (List String) )
decodePuzzleInput puzzleInput =
    let
        stacks =
            String.split "\n\n" puzzleInput
                |> List.head
                |> Maybe.withDefault " 1 "

        rearrangements =
            String.split "\n\n" puzzleInput
                |> List.tail
                |> Maybe.withDefault [ "" ]
                |> List.head
                |> Maybe.withDefault ""
    in
    ( rearrangements |> decodeRearrangement
    , stacks |> decodestack
    )


decodestack : String -> Array (List String)
decodestack stacks =
    let
        lines =
            stacks |> String.split "\n"

        lastLine =
            lines
                |> List.reverse
                |> List.head

        totalStacks =
            case lastLine of
                Just a ->
                    a
                        |> String.words
                        |> List.length

                Nothing ->
                    0

        crates =
            lines
                |> List.filter (String.contains "[")
    in
    List.range 0 (totalStacks - 1)
        |> List.map (takeStack crates)
        |> Array.fromList


takeStack : List String -> Int -> List String
takeStack crates stack =
    case crates of
        [] ->
            []

        x :: xs ->
            let
                crate =
                    String.slice (stack * 4 + 1) (stack * 4 + 2) x
            in
            if crate == " " then
                takeStack xs stack

            else
                crate :: takeStack xs stack


decodeRearrangement : String -> List ( Int, Int, Int )
decodeRearrangement rearrangements =
    rearrangements
        |> String.split "\n"
        |> List.map
            (\y ->
                y
                    |> String.split " "
                    |> List.filterMap String.toInt
                    |> (\x ->
                            case x of
                                [ count, from, to ] ->
                                    ( count, from, to )

                                _ ->
                                    ( 1, 1, 1 )
                       )
            )


moveCrate1 : ( List ( Int, Int, Int ), Array (List String) ) -> Array (List String)
moveCrate1 ( rearrangements, stacks ) =
    case rearrangements of
        [] ->
            stacks

        x :: xs ->
            let
                ( crateCount, fromStackNumber, toStackNumber ) =
                    x

                fromStack =
                    Array.get (fromStackNumber - 1) stacks

                toStack =
                    Array.get (toStackNumber - 1) stacks

                cratesToMove =
                    case fromStack of
                        Just stack ->
                            List.take crateCount stack |> List.reverse

                        Nothing ->
                            []

                newToStack =
                    case toStack of
                        Just stack ->
                            cratesToMove ++ stack

                        Nothing ->
                            []

                newFromStack =
                    case fromStack of
                        Just stack ->
                            List.drop crateCount stack

                        Nothing ->
                            []

                newStacksAndRearrangements =
                    ( xs
                    , stacks
                        |> Array.set (fromStackNumber - 1) newFromStack
                        |> Array.set (toStackNumber - 1) newToStack
                    )
            in
            moveCrate1 newStacksAndRearrangements


moveCrate2 : ( List ( Int, Int, Int ), Array (List String) ) -> Array (List String)
moveCrate2 ( rearrangements, stacks ) =
    case rearrangements of
        [] ->
            stacks

        x :: xs ->
            let
                ( crateCount, fromStackNumber, toStackNumber ) =
                    x

                fromStack =
                    Array.get (fromStackNumber - 1) stacks

                toStack =
                    Array.get (toStackNumber - 1) stacks

                cratesToMove =
                    case fromStack of
                        Just stack ->
                            List.take crateCount stack

                        Nothing ->
                            []

                newToStack =
                    case toStack of
                        Just stack ->
                            cratesToMove ++ stack

                        Nothing ->
                            []

                newFromStack =
                    case fromStack of
                        Just stack ->
                            List.drop crateCount stack

                        Nothing ->
                            []

                newStacksAndRearrangements =
                    ( xs
                    , stacks
                        |> Array.set (fromStackNumber - 1) newFromStack
                        |> Array.set (toStackNumber - 1) newToStack
                    )
            in
            moveCrate2 newStacksAndRearrangements


getFirstCrates : Array (List String) -> String
getFirstCrates stacks =
    stacks
        |> Array.toList
        |> List.map
            (\x ->
                List.head x
                    |> Maybe.withDefault " "
            )
        |> String.join ""


inputTest : String
inputTest =
    """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


input : String
input =
    """            [M] [S] [S]            
        [M] [N] [L] [T] [Q]        
[G]     [P] [C] [F] [G] [T]        
[B]     [J] [D] [P] [V] [F] [F]    
[D]     [D] [G] [C] [Z] [H] [B] [G]
[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
[P] [V] [S] [S] [B] [B] [Z] [M] [C]
[R] [H] [N] [P] [J] [Q] [B] [C] [F]
 1   2   3   4   5   6   7   8   9 

move 1 from 7 to 4
move 3 from 4 to 7
move 4 from 3 to 4
move 5 from 6 to 9
move 1 from 8 to 1
move 2 from 3 to 2
move 3 from 4 to 6
move 1 from 3 to 6
move 9 from 7 to 1
move 1 from 2 to 4
move 3 from 4 to 9
move 4 from 9 to 8
move 6 from 8 to 2
move 1 from 8 to 6
move 1 from 4 to 1
move 11 from 1 to 7
move 1 from 4 to 7
move 7 from 2 to 5
move 5 from 6 to 3
move 2 from 4 to 3
move 2 from 5 to 9
move 1 from 8 to 6
move 3 from 1 to 5
move 2 from 6 to 9
move 1 from 4 to 8
move 2 from 2 to 1
move 7 from 5 to 9
move 6 from 3 to 6
move 1 from 2 to 5
move 1 from 3 to 8
move 12 from 7 to 3
move 1 from 1 to 8
move 2 from 1 to 9
move 20 from 9 to 5
move 1 from 1 to 7
move 5 from 5 to 3
move 1 from 8 to 7
move 2 from 8 to 3
move 2 from 6 to 5
move 1 from 6 to 4
move 18 from 3 to 2
move 1 from 4 to 2
move 1 from 7 to 9
move 1 from 1 to 9
move 1 from 6 to 1
move 8 from 5 to 2
move 1 from 1 to 6
move 19 from 5 to 2
move 5 from 2 to 6
move 2 from 9 to 7
move 20 from 2 to 1
move 1 from 9 to 4
move 8 from 6 to 2
move 5 from 1 to 3
move 27 from 2 to 1
move 34 from 1 to 7
move 1 from 2 to 6
move 2 from 3 to 1
move 1 from 4 to 9
move 1 from 2 to 6
move 2 from 1 to 7
move 1 from 6 to 7
move 1 from 9 to 3
move 2 from 6 to 3
move 1 from 6 to 4
move 5 from 3 to 4
move 5 from 4 to 2
move 4 from 1 to 4
move 4 from 1 to 4
move 2 from 3 to 6
move 1 from 6 to 9
move 25 from 7 to 5
move 1 from 6 to 4
move 17 from 5 to 2
move 14 from 7 to 6
move 1 from 7 to 3
move 1 from 9 to 3
move 10 from 2 to 3
move 2 from 2 to 9
move 12 from 3 to 5
move 18 from 5 to 8
move 1 from 4 to 2
move 5 from 2 to 1
move 1 from 5 to 3
move 3 from 2 to 1
move 1 from 2 to 7
move 2 from 2 to 6
move 9 from 6 to 7
move 16 from 8 to 2
move 6 from 7 to 3
move 2 from 8 to 9
move 1 from 1 to 8
move 16 from 2 to 6
move 1 from 8 to 3
move 2 from 1 to 2
move 1 from 9 to 3
move 7 from 4 to 1
move 7 from 3 to 7
move 9 from 7 to 8
move 1 from 5 to 6
move 2 from 9 to 7
move 1 from 9 to 5
move 11 from 6 to 8
move 1 from 3 to 1
move 1 from 4 to 2
move 2 from 8 to 5
move 3 from 5 to 8
move 2 from 1 to 9
move 5 from 1 to 4
move 3 from 4 to 1
move 1 from 3 to 2
move 3 from 2 to 1
move 1 from 9 to 1
move 1 from 2 to 5
move 2 from 4 to 7
move 20 from 8 to 5
move 1 from 9 to 7
move 11 from 6 to 1
move 17 from 1 to 5
move 1 from 8 to 2
move 7 from 5 to 8
move 1 from 4 to 5
move 2 from 1 to 2
move 2 from 8 to 4
move 4 from 7 to 6
move 2 from 6 to 8
move 2 from 1 to 2
move 1 from 1 to 4
move 4 from 8 to 9
move 2 from 1 to 9
move 3 from 8 to 1
move 25 from 5 to 2
move 23 from 2 to 1
move 1 from 7 to 1
move 6 from 9 to 8
move 6 from 8 to 3
move 3 from 6 to 2
move 10 from 1 to 2
move 1 from 6 to 3
move 2 from 3 to 6
move 2 from 3 to 2
move 2 from 6 to 8
move 1 from 4 to 6
move 14 from 1 to 9
move 2 from 3 to 4
move 14 from 2 to 4
move 1 from 6 to 9
move 17 from 4 to 3
move 1 from 8 to 6
move 2 from 7 to 2
move 1 from 4 to 2
move 1 from 5 to 9
move 9 from 2 to 4
move 17 from 3 to 7
move 3 from 4 to 2
move 1 from 8 to 3
move 4 from 5 to 7
move 1 from 3 to 6
move 1 from 4 to 5
move 14 from 7 to 9
move 2 from 1 to 9
move 3 from 2 to 1
move 1 from 2 to 5
move 1 from 3 to 7
move 4 from 1 to 2
move 2 from 6 to 7
move 3 from 9 to 8
move 4 from 2 to 4
move 17 from 9 to 7
move 1 from 2 to 8
move 8 from 9 to 6
move 1 from 8 to 2
move 19 from 7 to 9
move 9 from 4 to 2
move 5 from 7 to 3
move 3 from 5 to 9
move 6 from 2 to 5
move 1 from 9 to 4
move 3 from 2 to 9
move 25 from 9 to 5
move 1 from 3 to 6
move 2 from 5 to 8
move 6 from 6 to 7
move 1 from 3 to 4
move 2 from 3 to 4
move 1 from 8 to 2
move 2 from 2 to 9
move 2 from 8 to 3
move 5 from 7 to 6
move 3 from 7 to 9
move 7 from 5 to 8
move 2 from 3 to 5
move 1 from 3 to 5
move 1 from 6 to 2
move 6 from 9 to 5
move 1 from 9 to 2
move 1 from 6 to 9
move 2 from 5 to 6
move 2 from 9 to 8
move 11 from 8 to 1
move 2 from 5 to 9
move 3 from 6 to 5
move 1 from 4 to 7
move 5 from 5 to 7
move 1 from 4 to 8
move 7 from 7 to 2
move 12 from 5 to 2
move 10 from 1 to 8
move 1 from 9 to 6
move 3 from 8 to 1
move 1 from 1 to 6
move 10 from 2 to 3
move 8 from 8 to 7
move 1 from 9 to 8
move 2 from 3 to 5
move 14 from 5 to 8
move 1 from 3 to 2
move 3 from 8 to 1
move 3 from 8 to 4
move 3 from 2 to 4
move 5 from 6 to 4
move 8 from 7 to 9
move 6 from 8 to 7
move 1 from 5 to 7
move 6 from 2 to 9
move 4 from 4 to 6
move 4 from 4 to 9
move 3 from 9 to 3
move 1 from 8 to 6
move 1 from 5 to 6
move 2 from 7 to 2
move 1 from 3 to 4
move 3 from 4 to 1
move 3 from 4 to 3
move 5 from 6 to 4
move 4 from 3 to 8
move 1 from 6 to 4
move 8 from 3 to 2
move 2 from 8 to 5
move 11 from 9 to 7
move 9 from 1 to 9
move 2 from 7 to 3
move 1 from 6 to 8
move 1 from 6 to 5
move 5 from 9 to 8
move 3 from 9 to 7
move 2 from 9 to 1
move 2 from 3 to 7
move 12 from 7 to 1
move 2 from 8 to 9
move 5 from 4 to 5
move 4 from 9 to 4
move 1 from 1 to 3
move 7 from 1 to 3
move 7 from 5 to 6
move 1 from 9 to 1
move 1 from 5 to 1
move 5 from 7 to 8
move 4 from 6 to 7
move 5 from 1 to 8
move 1 from 4 to 3
move 12 from 8 to 7
move 2 from 2 to 4
move 2 from 8 to 9
move 3 from 8 to 2
move 2 from 6 to 7
move 4 from 7 to 8
move 1 from 6 to 8
move 4 from 3 to 2
move 15 from 7 to 8
move 1 from 7 to 6
move 3 from 3 to 5
move 2 from 3 to 4
move 5 from 2 to 5
move 3 from 1 to 5
move 4 from 5 to 6
move 4 from 5 to 9
move 1 from 5 to 7
move 4 from 9 to 4
move 2 from 2 to 9
move 2 from 5 to 2
move 2 from 2 to 1
move 3 from 4 to 9
move 2 from 9 to 4
move 2 from 8 to 5
move 2 from 5 to 2
move 8 from 2 to 4
move 2 from 1 to 3
move 2 from 3 to 5
move 3 from 6 to 9
move 2 from 6 to 1
move 2 from 1 to 4
move 1 from 2 to 4
move 1 from 5 to 7
move 2 from 2 to 7
move 18 from 4 to 2
move 1 from 5 to 9
move 2 from 7 to 9
move 18 from 8 to 4
move 1 from 7 to 8
move 22 from 4 to 8
move 6 from 2 to 6
move 3 from 6 to 8
move 3 from 6 to 4
move 3 from 4 to 7
move 3 from 7 to 1
move 14 from 2 to 3
move 10 from 3 to 2
move 27 from 8 to 1
move 1 from 7 to 6
move 1 from 3 to 7
move 2 from 2 to 8
move 2 from 9 to 8
move 18 from 1 to 4
move 6 from 1 to 5
move 10 from 4 to 7
move 1 from 3 to 7
move 4 from 7 to 2
move 3 from 9 to 7
move 1 from 6 to 5
move 1 from 2 to 7
move 2 from 5 to 6
move 2 from 6 to 5
move 3 from 5 to 1
move 6 from 1 to 3
move 4 from 5 to 9
move 11 from 2 to 9
move 2 from 1 to 6
move 3 from 4 to 6
move 5 from 7 to 3
move 2 from 6 to 1
move 2 from 1 to 5
move 1 from 8 to 2
move 1 from 1 to 8
move 1 from 6 to 4
move 2 from 4 to 5
move 4 from 5 to 9
move 11 from 3 to 6
move 1 from 3 to 6
move 8 from 6 to 5
move 1 from 3 to 5
move 4 from 4 to 8
move 21 from 9 to 6
move 2 from 9 to 5
move 1 from 9 to 3
move 1 from 2 to 6
move 7 from 8 to 6
move 12 from 6 to 5
move 1 from 8 to 2
move 10 from 6 to 7
move 15 from 7 to 2
move 2 from 7 to 3
move 13 from 6 to 8
move 9 from 5 to 1
move 12 from 5 to 3
move 1 from 2 to 3
move 1 from 9 to 7
move 9 from 3 to 4
move 3 from 4 to 6
move 1 from 7 to 6
move 6 from 4 to 1
move 2 from 5 to 2
move 6 from 1 to 8
move 9 from 8 to 6
move 7 from 3 to 2
move 1 from 2 to 9
move 9 from 6 to 1
move 13 from 1 to 7
move 4 from 8 to 5
move 2 from 7 to 1
move 3 from 6 to 4
move 3 from 5 to 8
move 3 from 2 to 6
move 1 from 5 to 3
move 1 from 3 to 4
move 1 from 9 to 8
move 3 from 8 to 7
move 12 from 2 to 9
move 10 from 7 to 4
move 5 from 8 to 4
move 1 from 8 to 5
move 11 from 4 to 7
move 8 from 9 to 7
move 1 from 6 to 2
move 8 from 2 to 6
move 1 from 5 to 8
move 4 from 1 to 5
move 4 from 9 to 6
move 3 from 1 to 3
move 2 from 8 to 4
move 1 from 7 to 6
move 1 from 2 to 7
move 2 from 3 to 7
move 4 from 4 to 9
move 11 from 6 to 9
move 10 from 7 to 8
move 1 from 3 to 4
move 1 from 6 to 4
move 4 from 5 to 7
move 6 from 7 to 4
move 1 from 8 to 7
move 4 from 6 to 7
move 12 from 4 to 8
move 12 from 8 to 1
move 1 from 8 to 2
move 10 from 1 to 7
move 2 from 4 to 1
move 8 from 8 to 3
move 4 from 1 to 6
move 8 from 7 to 6
move 2 from 6 to 5
move 2 from 5 to 2
move 13 from 9 to 3
move 3 from 2 to 5
move 8 from 3 to 4
move 7 from 6 to 7
move 1 from 9 to 2
move 1 from 9 to 1
move 2 from 6 to 4
move 3 from 4 to 8
move 1 from 1 to 7
move 4 from 4 to 6
move 3 from 8 to 7
move 1 from 2 to 9
move 1 from 5 to 2
move 1 from 2 to 5
move 2 from 4 to 5
move 1 from 7 to 2
move 13 from 3 to 4
move 7 from 4 to 3
move 4 from 5 to 9
move 1 from 4 to 7
move 5 from 6 to 3
move 3 from 9 to 7
move 10 from 7 to 8
move 3 from 4 to 8
move 1 from 5 to 4
move 2 from 3 to 1
move 3 from 7 to 4
move 4 from 8 to 6
move 2 from 9 to 3
move 2 from 4 to 5
move 4 from 4 to 3
move 8 from 8 to 3
move 3 from 6 to 8
move 1 from 2 to 6
move 5 from 7 to 9
move 1 from 4 to 3
move 3 from 7 to 5
move 3 from 8 to 4
move 7 from 7 to 5
move 3 from 7 to 8
move 1 from 9 to 8
move 3 from 4 to 1
move 1 from 5 to 8
move 3 from 7 to 1
move 6 from 8 to 3
move 3 from 9 to 5
move 2 from 6 to 5
move 2 from 1 to 6
move 16 from 3 to 8
move 4 from 5 to 8
move 4 from 3 to 8
move 1 from 9 to 5
move 1 from 6 to 5
move 3 from 3 to 7
move 6 from 1 to 6
move 1 from 5 to 4
move 3 from 5 to 2
move 2 from 7 to 4
move 1 from 2 to 8
move 6 from 8 to 1
move 2 from 4 to 5
move 2 from 2 to 3
move 7 from 8 to 7
move 1 from 4 to 6
move 3 from 6 to 4
move 3 from 4 to 9
move 3 from 6 to 3
move 11 from 8 to 6
move 12 from 5 to 4
move 5 from 6 to 1
move 9 from 3 to 2
move 7 from 6 to 1
move 7 from 7 to 8
move 5 from 8 to 3
move 2 from 3 to 6
move 2 from 8 to 1
move 1 from 7 to 2
move 7 from 3 to 8
move 1 from 9 to 1
move 14 from 1 to 3
move 9 from 2 to 8
move 11 from 3 to 4
move 22 from 4 to 1
move 2 from 3 to 1
move 16 from 8 to 4
move 1 from 9 to 2
move 3 from 6 to 9
move 3 from 9 to 5
move 1 from 2 to 6
move 1 from 5 to 7"""
