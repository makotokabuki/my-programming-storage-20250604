#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
鶴亀算を解くPythonプログラム
作成日: 2025年6月4日
"""

def tsurukame_calculator(total_heads, total_legs):
    """
    鶴亀算を解く関数
    
    Args:
        total_heads (int): 頭の総数
        total_legs (int): 足の総数
    
    Returns:
        tuple: (鶴の数, 亀の数) または None（解がない場合）
    """
    # 鶴は足2本、亀は足4本
    # 鶴をx羽、亀をy匹とすると：
    # x + y = total_heads  ... (1)
    # 2x + 4y = total_legs ... (2)
    
    # (1)式からx = total_heads - y
    # これを(2)式に代入：2(total_heads - y) + 4y = total_legs
    # 2*total_heads - 2y + 4y = total_legs
    # 2*total_heads + 2y = total_legs
    # 2y = total_legs - 2*total_heads
    # y = (total_legs - 2*total_heads) / 2
    
    # 亀の数を計算
    kame_count = (total_legs - 2 * total_heads) / 2
    
    # 鶴の数を計算
    tsuru_count = total_heads - kame_count
    
    # 答えが整数で、かつ正の数かチェック
    if (kame_count >= 0 and tsuru_count >= 0 and 
        kame_count == int(kame_count) and tsuru_count == int(tsuru_count)):
        return int(tsuru_count), int(kame_count)
    else:
        return None

def main():
    """メイン関数"""
    print("=== 鶴亀算計算プログラム ===")
    print("鶴は足2本、亀は足4本です。")
    print()
    
    # 例題1: 頭が5個、足が14本の場合
    print("【例題1】")
    heads1 = 5
    legs1 = 14
    print(f"頭の数: {heads1}個")
    print(f"足の数: {legs1}本")
    
    result1 = tsurukame_calculator(heads1, legs1)
    if result1:
        tsuru, kame = result1
        print(f"答え: 鶴{tsuru}羽、亀{kame}匹")
        # 検算
        print(f"検算: 頭 = {tsuru} + {kame} = {tsuru + kame}個")
        print(f"      足 = {tsuru}×2 + {kame}×4 = {tsuru*2 + kame*4}本")
    else:
        print("この問題には解がありません。")
    print()
    
    # 例題2: 頭が10個、足が28本の場合
    print("【例題2】")
    heads2 = 10
    legs2 = 28
    print(f"頭の数: {heads2}個")
    print(f"足の数: {legs2}本")
    
    result2 = tsurukame_calculator(heads2, legs2)
    if result2:
        tsuru, kame = result2
        print(f"答え: 鶴{tsuru}羽、亀{kame}匹")
        # 検算
        print(f"検算: 頭 = {tsuru} + {kame} = {tsuru + kame}個")
        print(f"      足 = {tsuru}×2 + {kame}×4 = {tsuru*2 + kame*4}本")
    else:
        print("この問題には解がありません。")
    print()
    
    # ユーザー入力版
    print("【あなたも問題を解いてみましょう！】")
    try:
        user_heads = int(input("頭の数を入力してください: "))
        user_legs = int(input("足の数を入力してください: "))
        
        result = tsurukame_calculator(user_heads, user_legs)
        if result:
            tsuru, kame = result
            print(f"答え: 鶴{tsuru}羽、亀{kame}匹")
            print(f"検算: 頭 = {tsuru + kame}個, 足 = {tsuru*2 + kame*4}本")
        else:
            print("この問題には解がありません。数値を確認してください。")
            
    except ValueError:
        print("正しい数値を入力してください。")

if __name__ == "__main__":
    main()
