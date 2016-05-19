using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Driver;

namespace AppliedNoSqlSDD
{
	class Program
	{
		static void Main(string[] args)
		{
			InsertSomeData();
		}

		private static void InsertSomeData()
		{
			//Post p = new Post();
			//p.Title = "My first mongoDB example";
			//p.Url = "/go/mongo";
			Post p = new Post();
			p.Title = "Follow up on mongo";
			p.Url = "/go/mongo/2";

			var db = new Db();
			//db.Posts.InsertOne(p);

			var firstPost = db.Posts
				.AsQueryable()
				.First(post => post.Url == "/go/mongo/2");

			Console.WriteLine(firstPost.Title);
			// Console.WriteLine("Has {0} views", firstPost.ViewCount);
			//Console.WriteLine(firstPost.AddtionalData);

			//Comment c = new Comment();
			//c.CommentText = "Fantastic post, thanks";
			//c.Name = "Jeff";
			//firstPost.Comments.Add(c);

			//c = new Comment();
			//c.CommentText = "Great post, love it. Get your wordpress themes here: ...";
			//c.Name = "Sarah";
			//firstPost.Comments.Add(c);

			//db.Posts.ReplaceOne(ps => ps.Id == firstPost.Id, firstPost);


			//foreach (var post in db.Posts.AsQueryable())
			//{
			//	db.Posts.ReplaceOne(ps => ps.Id == post.Id, post);
			//}

			var jeffPosts =
				from pt in db.Posts.AsQueryable()
				where pt.Comments.Any(c => c.Name == "Jeff")
				select pt;

			Console.WriteLine("Jeffs Posts");
			foreach (var jp in jeffPosts)
			{

				Console.WriteLine(jp.Title);
			}

			var user = new User();
			user.Name = "root";
			db.Users.InsertOne(user);
		}
	}
}
