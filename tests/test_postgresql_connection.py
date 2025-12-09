#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试PostgreSQL数据库连接
"""

import os
import psycopg2
from psycopg2 import OperationalError
import sys

# 数据库配置（从.env文件读取）
DB_HOST = "127.0.0.1"
DB_PORT = 5444
DB_USER = "bettafish"
DB_PASSWORD = "bettafish123"
DB_NAME = "bettafish"
DB_DIALECT = "postgresql"

def test_connection():
    """测试PostgreSQL数据库连接"""
    print("=" * 60)
    print("PostgreSQL 数据库连接测试")
    print("=" * 60)

    # 显示连接配置
    print(f"主机地址: {DB_HOST}")
    print(f"端口号: {DB_PORT}")
    print(f"用户名: {DB_USER}")
    print(f"数据库名: {DB_NAME}")
    print("-" * 60)

    try:
        # 尝试连接数据库
        print("正在尝试连接数据库...")

        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        # 如果连接成功
        print("✅ 数据库连接成功！")

        # 创建游标
        cursor = conn.cursor()

        # 测试查询
        print("\n正在执行测试查询...")
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"数据库版本: {db_version[0]}")

        # 检查数据库中的表
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()

        if tables:
            print(f"\n发现 {len(tables)} 个表:")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("\n数据库中暂无表（可能需要初始化）")

        # 测试创建和删除
        print("\n测试基本操作...")
        cursor.execute("CREATE TABLE IF NOT EXISTS test_connection (id SERIAL PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
        cursor.execute("INSERT INTO test_connection (created_at) VALUES (CURRENT_TIMESTAMP);")
        cursor.execute("SELECT COUNT(*) FROM test_connection;")
        count = cursor.fetchone()[0]
        print(f"测试表记录数: {count}")

        # 清理测试数据
        cursor.execute("DROP TABLE IF EXISTS test_connection;")

        # 提交事务
        conn.commit()

        # 关闭连接
        cursor.close()
        conn.close()

        print("\n✅ 所有测试通过！数据库工作正常。")

    except OperationalError as e:
        print(f"❌ 数据库连接失败: {e}")
        print("\n可能的解决方案:")
        print("1. 确认PostgreSQL容器正在运行")
        print("2. 检查连接参数（主机、端口、用户名、密码）")
        print("3. 确认数据库已创建")
        print("4. 检查防火墙设置")
        return False

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

    return True

def check_docker_postgres():
    """检查Docker中的PostgreSQL状态"""
    print("\n" + "=" * 60)
    print("Docker PostgreSQL 容器状态")
    print("=" * 60)

    import subprocess

    try:
        # 检查PostgreSQL容器日志
        result = subprocess.run(
            ["docker", "logs", "postgres", "--tail", "10"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("PostgreSQL 容器最近日志:")
            print("-" * 40)
            print(result.stdout)

    except Exception as e:
        print(f"无法获取容器日志: {e}")

if __name__ == "__main__":
    success = test_connection()
    check_docker_postgres()

    if success:
        print("\n🎉 PostgreSQL 数据库连接测试成功！")
        sys.exit(0)
    else:
        print("\n💥 PostgreSQL 数据库连接测试失败！")
        sys.exit(1)